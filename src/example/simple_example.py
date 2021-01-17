from plugd.api import PlugdBase


class PlugdPlugin(PlugdBase):
    def __init__(self):
        """
        docstring
        """
        pass
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
        return 'simple_example'