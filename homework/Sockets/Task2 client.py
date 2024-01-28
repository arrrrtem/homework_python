import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    filename = input("Введите название файла: ")
    client.send(filename.encode('utf-8'))

    response = client.recv(1024)
    print(response.decode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
