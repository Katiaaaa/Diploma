import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


def load_model():
    preprocess_url = hub.load('https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/1')
    encoder_url = hub.load('https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/3')

    bert_preprocess = hub.KerasLayer(preprocess_url)
    bert_encoder = hub.KerasLayer(encoder_url)

    # Bert layers
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text_news')
    preprocessed_text = bert_preprocess(text_input)
    outputs = bert_encoder(preprocessed_text)

    # Neural network layers
    l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
    l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)

    # Use inputs and outputs to construct a final model
    model = tf.keras.Model(inputs=[text_input], outputs = [l])

    # Load trained weights
    model.load_weights("model_2.h5")

    return model