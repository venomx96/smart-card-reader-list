from distutils.core import setup
import py2exe
 
#import libraries that you imported in your target python file
import math
 
setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "script.py"}],
    zipfile = None,
)
