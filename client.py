import socket, time

HOST = "localhost"
PORT = 5000


# Confuguración de IP y puerto TCP del servidor y validación de disponibilidad
def validar_servidor():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            try:
                client_socket.connect((HOST, PORT))
                print("Conectado al servidor")
                break
            except ConnectionRefusedError:
                print("Servidor no disponible. Reintentando en 3 segundos...")
                time.sleep(3)
        return client_socket
    except Exception as e:
        print(f"Error al validar el servidor: {e}")


# Configuración de envio de mensajes al servidor
def configurar_mensajes(client_socket):
    try:
        while True:
            mensaje = input("-- ")
            client_socket.send(mensaje.encode())

            if mensaje.lower() == "salir":
                break

            data = client_socket.recv(1024)
            print(data.decode())

        client_socket.close()
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")


def main():
    cliente = validar_servidor()
    if cliente:
        configurar_mensajes(cliente)


if __name__ == "__main__":
    main()
