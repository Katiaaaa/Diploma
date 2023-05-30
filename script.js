function openTab(evt, tabName) {
	// Отримуємо всі вмістові елементи з класом "tabcontent"
	let tabcontents = document.getElementsByClassName("tabcontent");
	// Ховаємо їх усі
	for (let i = 0; i < tabcontents.length; i++) {
		tabcontents[i].style.display = "none";
	}
	// Отримуємо всі елементи з класом "tablinks"
	let tablinks = document.getElementsByClassName("tablinks");
	// Видаляємо клас "active" у всіх елементів з класом "tablinks"
	for (let i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	// Відображаємо вибраний вмістовий елемент
	document.getElementById(tabName).style.display = "block";
	// Додаємо клас "active" до натиснутого елемента з класом "tablinks"
	evt.currentTarget.className += " active";
}

function validateInput(input) {
	var regex = /^[a-zA-Zа-яА-ЯіїєІЇЄґҐ\s]+$/;
	if (!regex.test(input)) {
	  alert("Введені дані містять недопустимі символи. Будь ласка, введіть дані англійською або українською мовою.");
	  return false;
	}
	return true;
  }
function feetbackForm(evt){
	let name = document.getElementById("input1").value; // Отримуємо значення поля введення
	let email = document.getElementById("input2").value;
	let label = document.getElementById("input3").value;
	let news = document.getElementById("input").value;
	
	data = {
		name,
		email,
		news,
		label
	}
	fetch('http://127.0.0.1:5000/save-news', {
		method: 'POST',
		body: JSON.stringify(data),
		headers: { 'Content-Type': 'application/json' },
	})
}
function submitForm(evt) {

	document.getElementById("feetback").style.display = "block";
	evt.preventDefault(); // Зупиняємо стандартну поведінку форми
	let input = document.getElementById("input").value; // Отримуємо значення поля введення
	let output = document.getElementById("result"); // Отримуємо елемент, де будемо відображати відповідь

	var regex = /^[a-zA-Zа-яА-ЯіїєІЇЄґҐ0-9.,\"'\- ()ʼ]+$/;
	if (!regex.test(input)) {
		return alert("Введені дані містять недопустимі символи. Будь ласка, введіть дані англійською або українською мовою.");
	}
	// Відправляємо запит на сервер
	data = { data: input }
	fetch('http://127.0.0.1:5000/bert', {
		method: 'POST',
		body: JSON.stringify(data),
		headers: { 'Content-Type': 'application/json' },
	})
	.then(response => response.json())
	.then(data => {
		output.innerText = data;
		console.log(data);
	})
	  .catch(error => console.error(error));
}


	
