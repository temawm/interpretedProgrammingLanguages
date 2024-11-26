import cgi
import sqlite3

print("Content-Type: text/html")
print()
# Получаем данные из формы
form = cgi.FieldStorage()
policy_number = form.getvalue('policy_number')
client_id = form.getvalue('client_id')
policy_type = form.getvalue('policy_type')
start_date = form.getvalue('start_date')
end_date = form.getvalue('end_date')

# Подключаемся к базе данных и добавляем полис
conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Policies (policy_number, client_id, policy_type, start_date, end_date) VALUES (?, ?, ?, ?, ?)",
               (policy_number, client_id, policy_type, start_date, end_date))
conn.commit()
conn.close()

print("<h1>Полис добавлен!</h1>")
print("<a href='/index.html'>Вернуться на главную страницу</a>")