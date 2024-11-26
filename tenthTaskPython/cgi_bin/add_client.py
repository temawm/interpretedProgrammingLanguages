import cgi
import sqlite3

print("Content-Type: text/html")
print()

# Получаем данные из формы
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')

# Подключаемся к базе данных и добавляем клиента
conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Clients (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
conn.commit()
conn.close()

print("<h1>Клиент добавлен!</h1>")
print("<a href='/index.html'>Вернуться на главную страницу</a>")