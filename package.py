name = "plugd"

version = "0.0.3"

authors = [
    "arjun.thekkumadathil"
]

description = \
    """
    Configuration based plugin system written in python, no external module depen
    """
    
with scope("config") as c:
    c.release_packages_path = "Z:/packages/internal"

requires = ["~python-2.7"]

uuid = "rez-internal.plugd"

build_command = 'python {root}/rezbuild.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/src")
