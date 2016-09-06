# controller.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import ujson
from lib.modes import *
from lib.util import send
from lib.operations import *

class Controller(object):
    def __init__(self):
        self._devices = {}
    
    def add(self, device):
        if not device:
            return
        try:
            index = device.get_index() 
            if index != None:
                self._devices.update({index:device})
        except:
            pass
    
    def find(self, index):
        return self._devices.get(index)
    
    def mount(self):
        info = {}
        for i in self._devices:
            info.update({i:self._devices[i].get_profile()})
        send(info)
    
    def process(self, index, op, args):
        if op not in OP:
            return
        device = self._devices.get(index)
        if not device:
            return
        ret = None
        try:
            if op == OP_GET:
                ret = device.get()
            elif op == OP_PUT:
                ret = device.put(args)
            elif op == OP_OPEN:
                device.open()
            elif op == OP_CLOSE:
                device.close()
            if ret != None:
                send(ret)
        except:
            pass
    
    def trig(self):
        results = {}
        try:
            for i in self._devices:
                device = self._devices[i]
                if device.get_mode() & MODE_TRIG:
                    ret = device.get()
                    if ret != None:
                        results.update({i:ret})
        except:
            pass
        
        if results:
            send(results)
    
    def poll(self):
        results = {}
        try:
            for i in self._devices:
                device = self._devices[i]
                if device.get_mode() & MODE_POLL:
                    ret = device.get()
                    if ret != None:
                        results.update({i:ret})
        except:
            pass
        
        if results:
            send(results)
