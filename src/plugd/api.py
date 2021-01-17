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
        self._errors = []
        self._skip_error = False

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

    def is_valid(self):
        """
        Checks if the plugin is valid based on error skip error propeties

        Return: bool
        """
        if self.errors:
            if self.skip_error:
                return True
            else:
                return False
        else:
            return True

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

    @property
    def skip_error(self):
        """
        docstring
        """
        return self._skip_error

    @skip_error.setter
    def skip_error(self, value):
        """
        docstring
        """
        self._skip_error = value

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

    def is_valid_plugin(self, plugin_instance):
        """
        Checks if the plugin is inherited from PlugdBase class
        """
        try:
            if plugin_instance.is_plugd_base:
                return True
        except AttributeError:
            return False

    def get_plugin_module(self, module_package):
        """
        docstring
        """
        mod = importlib.import_module(module_package)
        return mod


    def run_plugin(self, plugin_name):
        """
        docstring
        """
        mod = self.get_plugin_module(self.config['plugins'][plugin_name])
        plugin_instance = mod.PlugdPlugin()
        if self.is_valid_plugin(plugin_instance):
            plugin_instance.run()

    def run_plugins(self):
        """
        Runs all plugins listed in the config
        """
        for plugin in self.config['plugins']:
            mod = self.get_plugin_module(self.config['plugins'][plugin])
            plugin_instance = mod.PlugdPlugin()
            if self.is_valid_plugin(plugin_instance):
                plugin_instance.run()

    def list_plugins(self):
        """
        List all plugins from the config
        """
        for plugin in self.config['plugins']:
            print("{0}: {1}".format(plugin, self.config['plugins'][plugin]))

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