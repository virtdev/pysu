# dust.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import pyb
from lib.modes import *
from lib.pulse import *
from dev.driver import Driver

INTERVAL = 30000 # ms

class Dust(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_POLL | MODE_SYNC | MODE_OUT | MODE_VISI, freq=0.01, spec={'dust':{'type':'int', 'range':[0, 1000], 'unit':'ug/m3'}})
        self._input = pyb.Pin(name, pyb.Pin.IN)
        self._start = pyb.millis()
        self._occupancy = 0
        self._result = 0

    def get(self):
        duration = pulseIn(self._input, LOW)
        if duration:
            self._occupancy += duration
        t = pyb.elapsed_millis(self._start)
        if t > INTERVAL:
            ratio = self._occupancy / (INTERVAL * 10.0)
            concentration = 1.1 * pow(ratio, 3) - 3.8 * pow(ratio, 2) + 520 * ratio + 0.62
            self._result = int(concentration * 0.0207916725464941)
            self._occupancy = 0
            self._start = pyb.millis()
        if self._result:
            return {'dust':self._result}
