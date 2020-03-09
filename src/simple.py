#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from cardboard import Vehicle, Motor

class Drive:
    def __init__(self):
        self.speed = 0.0
        self.m = Motor()

    def run(self, x):
        print("run", x)

    def update(self):
        print("update")
        #self.m.forward(self.speed)

    def run_threaded(self, x):
        if self.speed == x:
            return
        self.speed = x
        self.m.forward(x)

    def shutdown(self):
        self.speed = 0.0
        self.m.stop()
    

if __name__ == '__main__':
    v = Vehicle()

    v.mem['speed'] = 0.4

    drive = Drive()
    v.add(drive, inputs=['speed'], threaded=True)

    # start the drive loop at 10 Hz for 3 sec.
    v.start(rate_hz=10, max_loop_count=30, verbose=True)