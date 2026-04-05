# 💬 Chat Cliente-Servidor con Sockets en Python

## 📌 Descripción
Este proyecto consiste en la implementación de un sistema cliente-servidor utilizando sockets TCP en Python, con persistencia de datos en una base de datos SQLite.

El servidor recibe mensajes enviados por el cliente, los valida, los almacena en la base de datos junto con la fecha y la IP del cliente, y responde con una confirmación que incluye un timestamp.

El objetivo principal fue aplicar conceptos de:
- Comunicación cliente-servidor
- Programación con sockets TCP
- Persistencia de datos con SQLite
- Modularización del código
- Manejo de errores

### Servidor
- Escucha en `localhost:5000`
- Inicializa y verifica la base de datos automáticamente
- Acepta conexiones de clientes
- Recibe múltiples mensajes
- Valida que el mensaje no esté vacío
- Guarda cada mensaje en SQLite

Responde al cliente con:
- `Mensaje recibido: <timestamp>`
  
Maneja errores como:
- Puerto ocupado
- Base de datos no accesible

### Cliente
- Intenta conectarse al servidor con reintento automático si no está disponible
- Permite enviar múltiples mensajes
- Finaliza cuando el usuario escribe `salir`
- Muestra la respuesta enviada por el servidor para cada mensaje

### Base de Datos
Se utiliza SQLite para almacenar los mensajes en un archivo local chat.db

## 🚀 Tecnologías utilizadas
- Python 3
- Socket (TCP)
- SQLite3

## 🎯 Objetivo académico
Este proyecto fue desarrollado como práctica para comprender el funcionamiento de la comunicación en red, el manejo de sockets y la persistencia de información en aplicaciones cliente-servidor.
