

class Simulator:
    """
    This is a model represent an iot report data sender.
    """
    app_list = None

    def __init__(self, app_list):
        self.app_list = app_list

    def start(self):
        for app in self.app_list:
            app.start()
