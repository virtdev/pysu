# usd.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import pyb
from lib.modes import *
from lib.pulse import *
from dev.driver import Driver

D_MIN = 10
D_MAX = 100

class USD(Driver):
    def __init__(self, trig, echo):
        Driver.__init__(self, echo, mode=MODE_TRIG | MODE_VISI, spec={'enable':{}})
        self._echo = pyb.Pin(echo, pyb.Pin.IN)
        self._trig = pyb.Pin(trig, pyb.Pin.OUT_PP)
        self._trig.low()

    def get(self):
        self._trig.high()
        pyb.udelay(10)
        self._trig.low()
        d = pulseIn(self._echo, HIGH) / 29 / 2
        if d and d > D_MIN and d < D_MAX:
            return {'enable':True}
