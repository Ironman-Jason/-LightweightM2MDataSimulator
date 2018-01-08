import random


class Device:
    """
    This is a model represent an iot device, it contains a list of resource and device meta.
    """
    device_name = None
    device_sn = None
    resource_list = None

    def __init__(self, device_name, device_sn, resource_list):
        self.device_name = device_name
        self.device_sn = device_sn
        self.resource_list = resource_list

    def generate_report(self):
        if len(self.resource_list) is 0:
            return None
        index = random.randint(0, len(self.resource_list) - 1)
        report = self.resource_list[index].generate_callback_notification(device_sn=self.device_sn)
        return report
