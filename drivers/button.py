# button.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

from lib.modes import *
from dev.driver import Driver
from lib.interrupt import irq_rising

class Button(Driver):
    def __init__(self, name):
        Driver.__init__(self, name, mode=MODE_TRIG | MODE_VISI, spec={'enable':{}})
        irq_rising(name, self.callback)
    
    def get(self):
        if self.event.is_set():
            self.event.clear()
            return {'enable':True}
