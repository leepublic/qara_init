activate_this = '/home/www/venv-python2/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys
sys.path.insert(0, '/home/www/qarawww')
from run import app as application

