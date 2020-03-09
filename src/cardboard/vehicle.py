#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from .motors import Motors

# initialize the motors
print("Starting the engines ...")
motors = Motors(0.0)

print("Go!")

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  pass

# cleaning up
print("\Stopped.")