#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = serial_port_pkg.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2021, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__date__ = 30/4/23 15:18
__description__ = " "
__information__ : 
"""

import serial.tools.list_ports
import logging

def detect_serial_port():
    """
    Detectar el puerto serial al que se conecta automáticamente
    """
    com_ports = serial.tools.list_ports.comports()
    for port in com_ports:
        # /dev/cu.usbserial-145240
        if 'USB' in port.description or 'cu.usb' in port.description:
            return port.device
    return None


def get_data_acquisition():
    serial_port_connected = detect_serial_port()  # Puerto de lectura o escritura.

    if serial_port_connected is None:
        logging.error("No serial port found.")
        return None

    BAUD_RATE = 9600  # Velocidad de transmisión
    PARITY = serial.PARITY_NONE
    STOP_BITS = serial.STOPBITS_ONE
    BYTE_SIZE = serial.EIGHTBITS

    serial_port = serial.Serial(
        port=serial_port_connected,
        baudrate=BAUD_RATE,
        parity=PARITY,
        stopbits=STOP_BITS,
        bytesize=BYTE_SIZE,
        timeout=1.0  # Abrir el puerto serial, se establece un tiempo de espera de 1 seg
    )
    print("Conectado a: " + serial_port.portstr)

    while True:
        try:
            raw_data = serial_port.readline()  # leer una línea terminada '\n'
            # print(raw_data)
            if not raw_data:
                print("Desconectado Interfaz Serial")
                continue  # si quiere acabar el proceso poner break
            values = str(raw_data[0:len(raw_data)].decode("utf-8"))
            list_values = values.split(',')
            return list_values

        except KeyboardInterrupt:
            print("Comunicación Serial Interrumpida")
            break
    serial_port.close()  # cierre el puerto inmediatamente.

# print(serial_port_detected.__doc__)
# help(serial_port_detected)
