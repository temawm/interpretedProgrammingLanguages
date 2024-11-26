import cgi
import sqlite3

print("Content-Type: text/html")
print()

# Получаем данные из формы
form = cgi.FieldStorage()
policy_id = form.getvalue('policy_id')
claim_date = form.getvalue('claim_date')
amount = form.getvalue('amount')
status = form.getvalue('status')

# Подключаемся к базе данных и добавляем страховой случай
conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Claims (policy_id, claim_date, amount, status) VALUES (?, ?, ?, ?)",
               (policy_id, claim_date, amount, status))
conn.commit()
conn.close()

print("<h1>Страховой случай добавлен!</h1>")
print("<a href='/index.html'>Вернуться на главную страницу</a>")