import serial
import threading

# Configuración del primer puerto serie
ser1 = serial.Serial('/dev/ttyUSB0', 9600)

# Configuración del segundo puerto serie
ser2 = serial.Serial('/dev/ttyUSB1', 9600)

# Función para leer datos del primer puerto serie
def read_serial1():
    while True:
        if ser1.in_waiting:
            data = ser1.readline().decode('utf-8').rstrip()
            print(f'Serial 1: {data}')

# Función para leer datos del segundo puerto serie
def read_serial2():
    while True:
        if ser2.in_waiting:
            data = ser2.readline().decode('utf-8').rstrip()
            print(f'Serial 2: {data}')

# Creación de los hilos para leer los puertos serie
t1 = threading.Thread(target=read_serial1)
t2 = threading.Thread(target=read_serial2)

# Inicio de los hilos
t1.start()
t2.start()

# Espera a que los hilos terminen
t1.join()
t2.join()
