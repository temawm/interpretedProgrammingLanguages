from http.server import CGIHTTPRequestHandler, HTTPServer

# Определение порта, на котором будет работать сервер
PORT = 8000

# Создание сервера
server = HTTPServer(('localhost', PORT), CGIHTTPRequestHandler)
print(f"Сервер запущен на порту {PORT}. Для остановки нажмите Ctrl+C.")
server.serve_forever()

