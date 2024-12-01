import socket
import os
import json

s = socket.socket()
host = ''
port = 5000
s.bind((host, port))
s.listen(5)

def get_core_temp():
    return os.popen('vcgencmd measure_temp').readline().strip()

def get_voltage():
    return os.popen('vcgencmd measure_volts core').readline().strip()

def get_clock_speed():
    return os.popen('vcgencmd measure_clock arm').readline().strip()

def get_mem_gpu():
    return os.popen('vcgencmd get_mem gpu').readline().strip()

def get_mem_arm():
    return os.popen('vcgencmd get_mem arm').readline().strip()

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    data = {
        "Temperature": get_core_temp(),
        "Voltage": get_voltage(),
        "Clock_Speed": get_clock_speed(),
        "GPU_Memory": get_mem_gpu(),
        "ARM_Memory": get_mem_arm()
    }
    res = json.dumps(data).encode('utf-8')
    c.send(res)
    c.close()