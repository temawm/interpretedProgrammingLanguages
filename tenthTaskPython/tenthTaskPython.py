import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

# # Создаем таблицы
# cursor.execute('''
# CREATE TABLE Clients (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     phone TEXT
# )
# ''')
#
# cursor.execute('''
# CREATE TABLE Policies (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     policy_number TEXT NOT NULL UNIQUE,
#     client_id INTEGER,
#     policy_type TEXT NOT NULL,
#     start_date DATE NOT NULL,
#     end_date DATE NOT NULL,
#     FOREIGN KEY (client_id) REFERENCES Clients (id)
# )
# ''')
#
# cursor.execute('''
# CREATE TABLE Claims (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     policy_id INTEGER,
#     claim_date DATE NOT NULL,
#     amount REAL NOT NULL,
#     status TEXT NOT NULL,
#     FOREIGN KEY (policy_id) REFERENCES Policies (id)
# )
# ''')
#
# # Сохраняем изменения и закрываем соединение
# conn.commit()
# conn.close()





# conn = sqlite3.connect('insurance_company.db')
# cursor = conn.cursor()
#
# # Добавляем клиентов
# cursor.execute("INSERT INTO Clients (name, email, phone) VALUES ('Иван Иванов', 'ivan@example.com', '123456789')")
# cursor.execute("INSERT INTO Clients (name, email, phone) VALUES ('Мария Петрова', 'maria@example.com', '987654321')")
# cursor.execute("INSERT INTO Clients (name, email, phone) VALUES ('Сергей Смирнов', 'sergey@example.com', '555555555')")
#
# # Добавляем полисы
# cursor.execute("INSERT INTO Policies (policy_number, client_id, policy_type, start_date, end_date) VALUES ('POL12345', 1, 'Автострахование', '2023-01-01', '2024-01-01')")
# cursor.execute("INSERT INTO Policies (policy_number, client_id, policy_type, start_date, end_date) VALUES ('POL12346', 2, 'Медицинская страховка', '2023-02-01', '2024-02-01')")
# cursor.execute("INSERT INTO Policies (policy_number, client_id, policy_type, start_date, end_date) VALUES ('POL12347', 3, 'Недвижимость', '2023-03-01', '2024-03-01')")
#
# # Добавляем страховые случаи
# cursor.execute("INSERT INTO Claims (policy_id, claim_date, amount, status) VALUES (1, '2023-05-01', 10000.0, 'Обработан')")
# cursor.execute("INSERT INTO Claims (policy_id, claim_date, amount, status) VALUES (2, '2023-06-01', 5000.0, 'В ожидании')")
# cursor.execute("INSERT INTO Claims (policy_id, claim_date, amount, status) VALUES (3, '2023-07-01', 15000.0, 'Обработан')")
#
# conn.commit()
# conn.close()




conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

cursor.execute('''
SELECT Clients.name, COUNT(Policies.id) AS policy_count
FROM Clients
LEFT JOIN Policies ON Clients.id = Policies.client_id
GROUP BY Clients.id
''')

for row in cursor.fetchall():
    print(f"Клиент: {row[0]}, Количество полисов: {row[1]}")

conn.close()




conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

cursor.execute('''
SELECT Claims.claim_date, Claims.amount, Claims.status
FROM Claims
''')

for row in cursor.fetchall():
    print(f"Дата: {row[0]}, Сумма: {row[1]}, Статус: {row[2]}")

conn.close()

conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

cursor.execute('''
SELECT policy_number, end_date
FROM Policies
WHERE end_date BETWEEN '2024-01-01' AND '2024-12-31'
''')

for row in cursor.fetchall():
    print(f"Полис: {row[0]}, Дата окончания: {row[1]}")

conn.close()
