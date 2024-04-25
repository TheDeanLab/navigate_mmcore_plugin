# Standard Imports
import os
from pathlib import Path

# Third party imports
import pymmcore

from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import device_not_found, DummyDeviceConnection
from navigate.tools.file_functions import load_yaml_file


DEVICE_TYPE_NAME = "multiple_devices"
DEVICE_REF_LIST = ["type"]

mmcores = {}

def load_device(configuration, is_synthetic=False, device_type="stage"):
    """Build device connection.

    Returns
    -------
    device_connection : object
    """
    if is_synthetic:
        return DummyDeviceConnection()
    
    config_path = None
    if device_type in ["stage", "camera", "filter_wheel", "zoom"]:
        config_path = Path(configuration["config_path"])
    
    if not config_path:
        return None
    if config_path in mmcores.keys():
        mmc = mmcores[config_path]
    else:
        mmc = pymmcore.CMMCore()
        mmcores[config_path] = mmc
    if mmc.getProperty("Core", "Initialize") == "0":
        temp_path = os.path.abspath(__file__)
        for i in range(4):
            temp_path, _ = os.path.split(temp_path)
        device_config = load_yaml_file(os.path.join(temp_path, "plugin_config.yml"))
        mmc.setDeviceAdapterSearchPaths(device_config["device_adapter_path"])
        mmc.loadSystemConfiguration(str(config_path))

    return mmc


def start_device(microscope_name, device_connection, configuration, is_synthetic=False, device_type="stage", id=0):
    """Start device.

    Returns
    -------
    device_object : object
    """
    if is_synthetic:
        device_type_name = "synthetic"
    elif device_type in ["stage"]:
        device_type_name = configuration["configuration"]["microscopes"][microscope_name][
            device_type
        ]["hardware"][id]["type"]
        config_path = configuration["configuration"]["microscopes"][microscope_name][
            device_type
        ]["hardware"][id]["config_path"]
    else:
        device_type_name = configuration["configuration"]["microscopes"][microscope_name][
            device_type
        ]["hardware"]["type"]
        config_path = configuration["configuration"]["microscopes"][microscope_name][
            device_type
        ]["hardware"]["config_path"]

    if device_type_name != "MMCore":
        return device_not_found(microscope_name, device_type)

    if device_type == "stage":
        stage_device = load_module_from_file(
            "stage_device",
            os.path.join(Path(__file__).resolve().parent, "stage_device.py"),
        )
        if Path(config_path) not in mmcores:
            return device_not_found(microscope_name, "stage", "MMCore Config file path isn't right!")
        return stage_device.StageDevice(microscope_name, mmcores.get(Path(config_path), None), configuration, id)
    
    elif device_type == "shutter":
        shutter_device = load_module_from_file(
            "shutter_device",
            os.path.join(Path(__file__).resolve().parent, "shutter_device.py"),
        )
        return shutter_device.ShutterDevice(microscope_name, mmcores.get(Path(config_path), None), configuration)
    
    return device_not_found(microscope_name, device_type)
