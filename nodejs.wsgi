#!/usr/bin/python3
import sys

import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/nodejs/")
sys.path.insert(0,"/var/www/nodejs/nodejs/")

from nodejs import app as application
