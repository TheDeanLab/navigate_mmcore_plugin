from navigate.model.devices.shutter.laser_shutter_base import ShutterBase

class ShutterDevice(ShutterBase):
    def __init__(self, microscope_name, device_connection, configuration):
        """Initialize the Shutter.

        Parameters
        ----------
        microscope_name : str
            Name of microscope in configuration
        device_connection : object
            Hardware device to connect to
        configuration : multiprocesing.managers.DictProxy
            Global configuration of the microscope
        """
        super().__init__(microscope_name, device_connection, configuration)
        
        self.mmcore = device_connection

        if not self.mmcore.getShutterDevice():
            raise Exception(
                f"MMCore shutter isn't specified! "
                "Please set it in MMCore and update the cfg file!"
            )
        self.mmcore.setAutoShutter(False)

    def open_shutter(self):
        """Open the Shutter."""
        try:
            self.mmcore.setShutterOpen(True)
        except:
            print("Warning: Open MMCore shutter failed!")
        self.shutter_state = True

    def close_shutter(self):
        """Close the Shutter."""
        try:
            self.mmcore.setShutterOpen(False)
        except:
            print("Warning: Close MMCore shutter failed!")
        self.shutter_state = False