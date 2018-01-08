from iotreportsimulator.model.simulator import Simulator
from iotreportsimulator.model.application import Application
from iotreportsimulator.model.device import Device
from iotreportsimulator.model.resource import Resource

import logging


class ModelBuilder:
    def __init__(self):
        pass

    def build_simulator(self, conf):
        try:
            apps_conf = conf["nbi_app_services"]
        except KeyError as e:
            logging.info('parameter missing in conf.json file.', e)
            return None
        except TypeError as e:
            logging.info('please check your conf.json file.', e)
            return None
        application_list = self.build_applications(apps_conf)
        simulator = Simulator(app_list=application_list)
        return simulator

    def build_applications(self, apps_conf):
        application_list = []
        for app_conf in apps_conf:
            application = self.build_application(app_conf)
            if application is not None:
                application_list.append(application)
        return application_list

    def build_application(self, app_conf):
        try:
            app_name = app_conf["app_name"]
            host = app_conf["host"]
            port = app_conf["port"]
            callback_url = app_conf["callback_url"]
            devices_conf = app_conf["devices"]
        except KeyError as e:
            logging.info('parameter missing in conf.json file.', e)
            return None
        except TypeError as e:
            logging.info('please check your conf.json file.', e)
            return None
        device_list = self.build_devices(devices_conf)
        application = Application(app_name=app_name, host=host, port=port, callback_url=callback_url,
                                  devices_list=device_list)
        return application

    def build_devices(self, devices_conf):
        device_list = []
        for device_conf in devices_conf:
            device = self.build_device(device_conf)
            if device is not None:
                device_list.append(device)
        return device_list

    def build_device(self, device_conf):
        try:
            device_name = device_conf["device_name"]
            device_sn = device_conf["device_sn"]
            resources_conf = device_conf["resource"]
        except KeyError as e:
            logging.info('parameter missing in conf.json file.', e)
            return None
        except TypeError as e:
            logging.info('please check your conf.json file.', e)
            return None
        resource_list = self.build_resources(resources_conf)
        device = Device(device_name=device_name, device_sn=device_sn, resource_list=resource_list)
        return device

    def build_resources(self, resources_conf):
        resource_list = []
        for resource_conf in resources_conf:
            resource = self.build_resource(resource_conf)
            if resource is not None:
                resource_list.append(resource)
        return resource_list

    def build_resource(self, resource_conf):
        try:
            resource_name = resource_conf["resource_name"]
            resource_path = resource_conf["resource_path"]
            value_format = resource_conf["value_format"]
            value_candidates = resource_conf["value_candidates"]
            value_range = resource_conf["value_range"]
        except KeyError as e:
            logging.info('parameter missing in conf.json file.', e)
            return None
        except TypeError as e:
            logging.info('please check your conf.json file.', e)
            return None

        try:
            resource_path_variable_candidates = resource_conf["resource_path_variable_candidates"]
        except KeyError:
            resource_path_variable_candidates = None

        resource = Resource(resource_name=resource_name, resource_path=resource_path, value_format=value_format,
                            value_candidates=value_candidates, value_range=value_range,
                            resource_path_variable_candidates=resource_path_variable_candidates)
        return resource
