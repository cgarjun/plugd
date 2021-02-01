from abc import ABCMeta, abstractmethod, abstractproperty
import json
import importlib

__all__ = ['PlugdBase', 'Plugd']

class PlugdBase(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        """
        docstring
        """
        self._name = 'plugin_name'

    @abstractmethod
    def __str__(self):
        """
        docstring
        """
        pass

    @abstractmethod
    def run(self):
        """
        docstring
        """
        pass

    @abstractproperty
    def name(self):
        """
        Return: str
        """
        return self._name

    @abstractproperty
    def description(self):
        """
        Return: str
        """
        return self._description

    @property
    def is_plugd_base(self):
        """
        docstring
        """
        return True


class Plugd(object):
    def __init__(self, file_path):
        """
        Example plugin config structure given below
        {
            "plugins":{
                        "simple_example":"example.simple_example"
                    }
        }
        """
        self._file_path = file_path
        self._config = None

        with open(file_path) as json_file:
            self._config = json.load(json_file)

    def _run_plugin(self, plugin_instance):
        """
        docstring
        """
        if self.is_valid_plugin(plugin_instance):
            try:
                plugin_instance.run()
            except Exception as e:
                if break_on_error:
                    raise e
                self.errors = e

    def is_valid_plugin(self, plugin_instance):
        """
        Checks if the plugin is inherited from PlugdBase class
        """
        try:
            if plugin_instance.is_plugd_base:
                return True
        except AttributeError:
            return False

    def get_plugin(self, plugin_name):
        """
        docstring
        """
        mod = self.get_plugin_module(plugin_name)
        plugin_instance = mod.PlugdPlugin()
        return plugin_instance

    def get_plugins():
        """
        docstring
        """
        plugins = []
        for plugin in self.config['plugins']:
            plugins.append(self.get_plugin(plugin))

        return plugins

    def get_plugin_module(self, plugin_name):
        """
        docstring
        """
        module_package = self.config['plugins'][plugin_name]
        mod = importlib.import_module(module_package)
        return mod


    def run_plugin(self, plugin_name):
        """
        docstring
        """
        plugin_instance = self.get_plugin(plugin_name)
        self._run_plugin(plugin_instance)
        return plugin_instance

    def run_plugins(self):
        """
        Runs all plugins listed in the config
        """
        for plugin in self.config['plugins']:
            self.run_plugin(plugin)

        return True

    def list_plugins(self):
        """
        List all plugins from the config
        Return: dict
        """
        return self.config['plugins']

    @property
    def file_path(self):
        """
        docstring
        """
        return self._file_path

    @property
    def config(self):
        """
        docstring
        """
        return self._config

    @property
    def errors(self):
        """
        Return: list
        """
        return self._errors

    @errors.setter
    def errors(self, value):
        """
        Append an error to the error list
        
        Parameters
        -------------------------------------------------------------
        value: str
            Error string
        """
        return self._errors.append(value)