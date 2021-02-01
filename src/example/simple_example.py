from plugd.api import PlugdBase


class PlugdPlugin(PlugdBase):
    def __init__(self):
        """
        docstring
        """
        self._name = 'Simple Plugin'
        self._description = 'Simple Plugin'
    def __str__(self):
        """
        docstring
        """
        return "simple_example plugin"
        
    def run(self):
        """
        docstring
        """
        print("Simple example plugin")

    @property
    def name(self):
        """
        docstring
        """
        return self._name

    @property
    def description(self):
        """
        docstring
        """
        return self._description