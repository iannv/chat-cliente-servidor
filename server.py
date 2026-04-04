import socket
from datetime import datetime
from database import conexion_sqlite

HOST = 'localhost'
PORT = 5000

# FALTA MODULARIZAR EN 2 FUNCIONES

try:
    # Configuración de IP y puerto TCP del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    # Conexión a la base de datos
    conexion_sqlite.crear_tabla()
    
    # Recibir la conexión del cliente
    server_socket.listen(1)
    print('Esperando conexión del cliente...')
    conn_cliente, addr_cliente = server_socket.accept()

    while True:
        data = conn_cliente.recv(1024)
        if not data:
            break
        mensaje = data.decode()
        print("Mensaje recibido: ", mensaje)
        
        if mensaje.lower() == 'salir':
            break
        
        if not mensaje.strip():
            conn_cliente.send('**** Mensaje vacío no permitido ****'.encode())
            continue
        conexion_sqlite.guardar_mensaje(mensaje, addr_cliente[0])
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        respuesta = f'Mensaje recibido: {timestamp}'
        conn_cliente.send(respuesta.encode())
        
    conn_cliente.close()

# Validaciones de puerto y error en la base de datos
except OSError as e:
    print(f'Error {e} - El puerto {PORT} ya está en uso')

except Exception as e:
    print(f'Error en la base de datos: {e}')