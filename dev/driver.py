from lib.event import Event
from lib.util import name2index

class Driver(object):
    def __init__(self, name, mode=0, rng=None, freq=None):
        self.__mode = 0
        self.__name = name
        self.__freq = None
        self.__range = None
        self.event = Event()
        self.__index = name2index(name)
    
    def __str__(self):
        return self.__class__.__name__
    
    def get_name(self):
        return self.__name
    
    def get_mode(self):
        return self.__mode
    
    def get_index(self):
        return self.__index
    
    def get_info(self):
        ret = {'type':str(self), 'mode':self.__mode}
        if self.__freq:
            ret.update({'freq':self.__freq})
        if self.__range:
            ret.update({'range':self.__range})
        return ret
    
    def callback(self):
        self.event.set()
    
    def open(self):
        pass
    
    def close(self):
        pass
    
    def get(self):
        pass
    
    def put(self, args):
        pass
    