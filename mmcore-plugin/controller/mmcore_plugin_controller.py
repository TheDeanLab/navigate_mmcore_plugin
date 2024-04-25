import os
from tkinter import messagebox

from navigate.tools.file_functions import load_yaml_file, save_yaml_file


class MmcorePluginController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller

        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        self.buttons["confirm"].configure(command=self.update_path)

        temp_path = os.path.abspath(__file__)
        for i in range(2):
            temp_path, _ = os.path.split(temp_path)

        self.plugin_config_path = temp_path
        self.device_config = load_yaml_file(
            os.path.join(self.plugin_config_path, "plugin_config.yml")
        )
        self.variables["mmcore_path"].set(self.device_config["device_adapter_path"][0])

    def update_path(self, *args):
        """update device adapter path"""
        self.device_config["device_adapter_path"] = [
            self.variables["mmcore_path"].get()
        ]
        save_yaml_file(
            self.plugin_config_path, self.device_config, filename="plugin_config.yml"
        )
        messagebox.showinfo(
            title="MMCore Plugin",
            message="MMCore Dll Path is updated! Please restart navigate!",
        )
