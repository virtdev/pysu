import ujson
from lib.op import *
from lib.mode import *
from lib.util import send

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
            info.update({i:self._devices[i].get_info()})
        send(info)
    
    def process(self, index, op, args):
        if op not in Operations:
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
