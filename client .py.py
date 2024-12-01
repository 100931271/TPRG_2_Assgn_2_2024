import socket
import json

s = socket.socket()
host = '192.168.2.69'
port = 5000

try:
    s.connect((host, port))
    print("Connected to the server.")
except Exception as e:
    print(f"Error connecting to server: {e}")
    exit()

try:
    data = s.recv(1024).decode('utf-8')
    s.close()

    json_data = json.loads(data)
    print("\nReceived Data:")
    for key, value in json_data.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"Error receiving data: {e}")
    s.close()
