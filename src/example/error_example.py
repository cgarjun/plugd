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
        return "error_example plugin"
    def run(self):
        """
        docstring
        """
        raise IOError("This shows an example error")

    @property
    def name(self):
        """
        docstring
        """
        return 'error_example'