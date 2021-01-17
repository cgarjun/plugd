# plugd
Configuration based python plugin management

<p align="left">
  <img src="https://github.com/cgarjun/plugd/blob/main/plugd.jpg" width="150" title="hover text">
</p>

## Config schema
config.json
```
{
    "plugins":{
        "simple_example":"example.simple_example",
        "another_example":"example.another_example",
        }
}
```

## Usage
```
from plugd.api import Plugd
plug = Plugd('config.json')
plug.run_plugins()
```
## Plugin Structure
Example direcotry to be available through PYTHONPATH
```
example
|_______ simple_example.py
|_______ error_example.py
|_______ __init__.py
```
## Example plugin
```
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
```