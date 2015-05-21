from lib.event import Event
from lib.util import pin2index

class Driver(object):
    def __init__(self, pin):
        self.__pin = pin
        self.__mode = 0
        self.__freq = None
        self.__range = None
        self.event = Event()
        self.__index = pin2index(pin)
    
    def set(self, mode=0, rng=None, freq=None):
        self.__mode = mode
        self.__freq = freq
        self.__range = rng
    
    def __str__(self):
        return self.__class__.__name__
    
    def get_mode(self):
        return self.__mode
    
    def get_index(self):
        return self.__index
    
    def get_pin(self):
        return self.__pin
    
    def get_info(self):
        ret = {'type':str(self), 'mode':self.__mode}
        if self.__freq:
            ret.update({'freq':self.__freq})
        if self.__range:
            ret.update({'range':self.__range})
        return ret
    
    def callback(self):
        self.event.set()
    
    def setup(self):
        pass
    
    def open(self):
        pass
    
    def close(self):
        pass
    
    def get(self):
        pass
    
    def put(self, args):
        pass
    