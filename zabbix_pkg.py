#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = zabbix_pkg.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2023, IG-EPN"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__date__ = 29/4/23 15:15
__description__ = " "
__information__ : 
"""

from pyzabbix import ZabbixMetric, ZabbixSender
import logging
import tilt_utils
import sys


def connect_to_zabbix(zx_ip, zx_port):
    """
    Try to connect to a zabbix server.

    :return:
    :param zx_ip: str
    :param zx_port: int
    :return: ZabbixSender object
    """

    try:
        return ZabbixSender(zx_ip, zx_port)
    except Exception as e:
        raise Exception("Error in connect_to_zabbix: %s" % str(e))


def send_to_zabbix(zx_server, x):

    """
    Receive soh_data array and send it to a zabbix trigger item only  if ping ok

    :param zx_server:
    :param x: list
    :return: None
    """

    print(x)
    axis_x = x[0]
    # hostname = "CAYA_FW_1"
    try:
        run_param = tilt_utils.read_parameters(sys.argv[1])
    except Exception as e:
        logging.error("Error reading configuration file: %s" % str(e))
        raise Exception("Error reading configuration file: %s" % str(e))

    hostname = run_param['hostname']['host']
    metrics = [
        ZabbixMetric(hostname, 'axis.x.data', axis_x[1:]),
        ZabbixMetric(hostname, 'axis.y.data', x[1]),
        ZabbixMetric(hostname, 'temperature.data', x[2]),
        ZabbixMetric(hostname, 'serial.number.data', x[3])
    ]
    try:
        res = zx_server.send(metrics)
        logging.info("%s, %s" % (hostname, res))
    except Exception as e:
        logging.info("Error in send_to_zabbix. Error was: %s" % str(e))
