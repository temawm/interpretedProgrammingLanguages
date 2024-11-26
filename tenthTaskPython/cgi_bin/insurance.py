import cgi
import sqlite3
import json

print("Content-Type: text/html")
print()

# Функция для получения всех клиентов
def get_clients():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

# Функция для получения всех полисов
def get_policies():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Policies")
    policies = cursor.fetchall()
    conn.close()
    return policies

# Функция для получения всех страховых случаев
def get_claims():
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Claims")
    claims = cursor.fetchall()
    conn.close()
    return claims

# Отображение клиентов
clients = get_clients()
print("<h1>Клиенты</h1>")
print("<ul>")
for client in clients:
    print(f"<li>ID: {client[0]}, Имя: {client[1]}, Email: {client[2]}, Телефон: {client[3]}</li>")
print("</ul>")

# Отображение полисов
policies = get_policies()
print("<h1>Полисы</h1>")
print("<ul>")
for policy in policies:
    print(f"<li>ID: {policy[0]}, Номер полиса: {policy[1]}, ID клиента: {policy[2]}, Тип полиса: {policy[3]}, Дата начала: {policy[4]}, Дата окончания: {policy[5]}</li>")
print("</ul>")

# Отображение страховых случаев
claims = get_claims()
print("<h1>Страховые случаи</h1>")
print("<ul>")
for claim in claims:
    print(f"<li>ID: {claim[0]}, ID полиса: {claim[1]}, Дата: {claim[2]}, Сумма: {claim[3]}, Статус: {claim[4]}</li>")
print("</ul>")