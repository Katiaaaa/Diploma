import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
            'Server=DESKTOP-Q94UJ7E;'
            'Database=news;'
            'Trusted_Connection=yes;')

import datetime
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%H:%M:%S")


cursor = conn.cursor()
query = '''
INSERT INTO dbo.News(TextNews, [Date], [Time], Label, OriginId)
VALUES (, current_date, formatted_time, ?, 3)
'''

cursor.execute(query, 'My test news from Python', '2023-03-22', '13:00:00', '1') 

cursor.commit()

#row = cursor.fetchone()  
#while row:  
#    print(str(row[0]))     
#    row = cursor.fetchone()  