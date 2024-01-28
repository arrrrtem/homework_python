"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
"""

import socket
import threading

def handle_client(client_socket):
    data = client_socket.recv(1024)
    filename = data.decode('utf-8')

    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            response = f"Содержание файла:\n{content}\nКоличество слов: {word_count}"
    except FileNotFoundError:
        response = "Файл не найден"

    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(5)
    print("Сервер запущен и слушает порт 5555")

    while True:
        client_socket, addr = server.accept()
        print(f"Принято соединение от {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
