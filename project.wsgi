#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/project/")
sys.path.insert(0,"/var/www/project/project/")

import logging
logging.basicConfig(stream=sys.stderr)

from project import app as application

