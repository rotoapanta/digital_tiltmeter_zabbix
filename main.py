#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = serial_port_detected.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2021, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__fecha__ = 4/2/22 22:25
__description__ = "Puertos seriales conectados y selección del puerto Prolific"
__information__ : https://qastack.mx/programming/12090503/listing-available-com-ports-with-python
"""


import tilt_utils
from zabbix_pkg import *
import os
import sys
import logging
from serial_port_pkg import *


def main():
    exec_dir = os.path.realpath(os.path.dirname(__file__))
    print(exec_dir)
    logging.basicConfig(
        format='%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
        level=logging.INFO,  # Nivel de los eventos que se registran en el logger
        filename=os.path.join(exec_dir, "inclino_logs_info5.log"),  # Fichero en el que se escriben los logs
        filemode="a"  # a ("append"), en cada escritura, si el archivo de logs ya existe,
        # se abre y añaden nuevas lineas.
    )
    is_error = False

    if len(sys.argv) == 1:
        is_error = True
    else:
        try:
            run_param = tilt_utils.read_parameters(sys.argv[1])
        except Exception as e:
            print(4)
            logging.error("Error reading configuration file: %s" % str(e))
            raise Exception("Error reading configuration file: %s" % str(e))

        try:
            print(5)
            zabbix_server = run_param['zabbix_server']['ip']
            zabbix_port = run_param['zabbix_server']['port']
        except Exception as e:
            logging.error("Error getting parameters: %s" % str(e))
            raise Exception("Error getting parameters: %s" % str(e))

        try:
            zx_server = connect_to_zabbix(zabbix_server, int(zabbix_port))

            x = get_data_acquisition()
            for n in range(3, len(x)):
                send_to_zabbix(zx_server, x)

        except Exception as e:
            logging.error("Error in main(): %s " % str(e))

        if is_error:
            logging.info(f'Usage: python {sys.argv[0]} configuration_file.txt ')
            print(f'Usage: python {sys.argv[0]} CONFIGURATION_FILE.txt ')


main()
