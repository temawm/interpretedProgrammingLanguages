import sqlite3
import json

print("Content-Type: application/json")
print()

conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

# Получаем данные клиентов
cursor.execute("SELECT * FROM Clients")
clients = cursor.fetchall()

# Преобразуем данные в словарь
clients_list = []
for client in clients:
    clients_list.append({
        "id": client[0],
        "name": client[1],
        "email": client[2],
        "phone": client[3]
    })

# Закрываем соединение
conn.close()

# Возвращаем данные в формате JSON
print(json.dumps(clients_list, ensure_ascii=False))