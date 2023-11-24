""" tk_utils API

         
"""

# Toolkit must be available

try: 
    from project2 import toolkit_config as tk_cfg
except ModuleNotFoundError:
    msg = '''Could not import the `toolkit_config` module

Please make sure this module is located directly under `toolkit`

    toolkit/                <- PyCharm project folder
    | ...
    |__ toolkit_config.py
'''
    raise ModuleNotFoundError(msg)






