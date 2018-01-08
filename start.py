#!/usr/bin/env python


from time import sleep
import logging
import json
from iotreportsimulator.model_builder import ModelBuilder


CONF_FILE = 'conf.json'
LOG_FILE = 'report_data_simulator.log'
lOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s %(message)s'
SENDING_INTERVAL = 2


def init_logger():
    logging.basicConfig(filename=LOG_FILE, level=lOG_LEVEL, format=LOG_FORMAT)
    logging.debug('Start sending report data.')


def load_data_from_conf():
    try:
        with open(CONF_FILE) as conf:
            data = json.load(conf)
    except IOError as e:
        print("Cannot find config file, simulator will exit.", e)
        return None
    except ValueError as e:
        print ("Wrong json configuration file. simulator will exit.", e)
        return None

    global LOG_FILE
    global SENDING_INTERVAL
    try:
        LOG_FILE = data["log_file"]
        SENDING_INTERVAL = data["sending_interval"]
    except KeyError as e:
        print("Use default report_data_simulator.log and default polling interval: 2 seconds.", e)
    return data


def start_simulator():
    init_logger()
    conf = load_data_from_conf()
    simulator_builder = ModelBuilder()
    simulator = simulator_builder.build_simulator(conf)
    if simulator is None:
        return

    while(True):
        sleep(SENDING_INTERVAL)
        simulator.start()


if __name__ == '__main__':
    start_simulator()
