import random
import time


class Resource:
    """
    This is a model represent iot device resource, it also generate report data according to
    configuration.
    """
    resource_name = None
    resource_path = None
    resource_path_variable_candidates = None
    value_format = None
    value_candidates = None
    value_range = None

    def __init__(self, resource_name, resource_path, resource_path_variable_candidates, value_format, value_candidates,
                 value_range):
        self.resource_name = resource_name
        self.resource_path = resource_path
        self.resource_path_variable_candidates = resource_path_variable_candidates
        self.value_format = value_format
        self.value_candidates = value_candidates
        self.value_range = value_range

    def generate_resource_path(self):
        if "*" not in self.resource_path:
            return self.resource_path
        if len(self.resource_path_variable_candidates) is not 0:
            index = random.randint(0, len(self.resource_path_variable_candidates) - 1)
            candidate = self.resource_path_variable_candidates[index]
            return self.resource_path.replace('*', str(candidate))
        else:
            return self.resource_path.replace('*', str(random.randint(0, 100)))

    def generate_value(self):
        if len(self.value_candidates) is not 0:
            index = random.randint(0, len(self.value_candidates) - 1)
            candidate = self.value_candidates[index]
            return self.value_format.replace('*', str(candidate))
        if len(self.value_range) >= 2:
            value = random.randint(self.value_range[0], self.value_range[1])
            return self.value_format.replace('*', str(value))
        if len(self.value_range) is 0:
            return self.value_format.replace('*', str(random.randint(0, 100)))

    def generate_timestamp(self):
        timestamp = long(int(round(time.time() * 1000)))
        return timestamp

    def generate_reports(self, device_sn):
        serial_number = device_sn
        subscription_id = '121212'
        payload = ''
        timestamp = self.generate_timestamp()
        resource_path = self.generate_resource_path()
        value = self.generate_value()
        report = {'serialNumber': serial_number, 'timestamp': timestamp, 'subscriptionId': subscription_id,
                  'resourcePath': resource_path, 'value': value, 'payload': payload}
        reports = [report]
        return reports

    def generate_callback_notification(self, device_sn):
        reports = self.generate_reports(device_sn=device_sn)
        deregistrations = None
        expirations = None
        registrations = None
        updates = None
        responses = None
        have_received_callback = True
        timeout = False
        callbacknotification = {'deregistrations': deregistrations, 'expirations': expirations,
                                'registrations': registrations, 'reports': reports, 'responses': responses,
                                'updates': updates, 'haveReceivedCallback': have_received_callback, 'timeout': timeout}
        return callbacknotification
