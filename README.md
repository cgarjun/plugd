# plugd
One of the main reason for the origin of this library was to make sure the system
remains really simple and don't have any crazy complicated workflows to setup a 
plugin.



<p align="left">
  <img src="https://github.com/cgarjun/plugd/blob/main/plugd.jpg" width="150" title="hover text">
</p>

## Config schema
config.json
```json
{
    "plugins":{
        "simple_example": "example.simple_example",
        "another_example": "example.error_example"
        }
}
```

## Usage
```python
from plugd.api import Plugd
plug = Plugd('config.json')
plug.run_plugins()
```
## Plugin Structure
Example direcotry to be available through PYTHONPATH
```bash
example
|_______ simple_example.py
|_______ error_example.py
|_______ __init__.py
```
## Example plugin
```python
from plugd.api import PlugdBase

class PlugdPlugin(PlugdBase):

    def __init__(self):
        pass

    def __str__(self):
        return "simple_example plugin"

    def run(self):
        print("Simple example plugin")

    @property
    def name(self):
        return 'simple_example'
```
## Tested platforms
|Python Version|OS Platforms|
|--------------------|--------------------|
|2.7|Windows 10|
|3.6|Mac Catalina 10.15.7|

## Unit Testing
```bash
https://github.com/cgarjun/plugd.git
cd plugd/src
python -m unittest test.test_api
```