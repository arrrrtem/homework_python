import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        message = input("Введите сообщение (для завершения введите 'Пока'): ")
        client.send(message.encode('utf-8'))

        if message == 'Пока':
            break

        response = client.recv(1024)
        print(f"Ответ от сервера: {response.decode('utf-8')}")

    client.close()

if __name__ == "__main__":
    main()
