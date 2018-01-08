import requests
import logging
import json
import random


class Application:
    """
    This is a model represent an iot nbi application, it contains a list of device and application meta.
    """
    app_name = None
    host = None
    port = None
    callback_url = None
    devices_list = None

    def __init__(self, app_name, host, port, callback_url, devices_list):
        self.app_name = app_name
        self.host = host
        self.port = port
        self.callback_url = callback_url
        self.devices_list = devices_list

    def start(self):
        report = self.generate_report()
        if report is not None:
            self.send_report(report=report)

    def generate_report(self):
        if len(self.devices_list) is 0:
            return None
        index = random.randint(0, len(self.devices_list) - 1)
        report = self.devices_list[index].generate_report()
        return report

    def send_report(self, report):
        url = "http://" + self.host + ":" + self.port + self.callback_url
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        params = json.dumps(report)
        result = requests.post(url, headers=headers, data=params)
        logging.debug(result)
