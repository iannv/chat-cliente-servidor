import socket
from datetime import datetime
from database import conexion_sqlite

HOST = "localhost"
PORT = 5000


# Configuración de IP y puerto TCP del servidor, recibir conexión del cliente y conectar a la base de datos
def inicializar_servidor():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))

        conexion_sqlite.crear_tabla()

        server_socket.listen(1)
        print("Esperando conexión del cliente...")
        return server_socket

    # Validaciones de puerto y error en la base de datos
    except OSError as e:
        print(f"Error {e} - El puerto {PORT} ya está en uso")

    except Exception as e:
        print(f"Error en la base de datos: {e}")


# Aceptar las conexiones del cliente
def aceptar_conexiones(server_socket):
    try:
        conn_cliente, addr_cliente = server_socket.accept()
        socket_cliente(conn_cliente, addr_cliente)
    except Exception as e:
        print(f"Error al aceptar conexión: {e}")


# Recibir mensajes del cliente, validar contenido, almacenar en la base de datos y enviar la confirmación con timestamp.
def socket_cliente(conn_cliente, addr_cliente):
    try:
        while True:
            data = conn_cliente.recv(1024)
            if not data:
                break
            mensaje = data.decode()
            print("Mensaje recibido: ", mensaje)

            if mensaje.lower() == "salir":
                break

            if not mensaje.strip():
                conn_cliente.send("**** Mensaje vacío no permitido ****".encode())
                continue
            conexion_sqlite.guardar_mensaje(mensaje, addr_cliente[0])
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            respuesta = f"Mensaje recibido: {timestamp}"
            conn_cliente.send(respuesta.encode())

        conn_cliente.close()
        
    except Exception as e:
        print(f"Error en el socket cliente: {e}")


def main():
    servidor = inicializar_servidor()
    if servidor:
        aceptar_conexiones(servidor)


if __name__ == "__main__":
    main()