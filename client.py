import socket, time

HOST = 'localhost'
PORT = 5000

# Configuración de IP y puerto TCP del servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Validación si el servidor no se encuentra disponible
while True:
    try:
        client_socket.connect((HOST, PORT))
        print("Conectado al servidor")
        break
    except ConnectionRefusedError:
        print("Servidor no disponible. Reintentando en 3 segundos...")
        time.sleep(3)

# Configuración del envio del mensaje del cliente al servidor
while True:
    mensaje = input("-- ")
    client_socket.send(mensaje.encode())
    
    if mensaje.lower() == 'salir':
        break
    
    data = client_socket.recv(1024)
    print(data.decode())
    
client_socket.close()