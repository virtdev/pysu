# driver.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

from lib.event import Event
from lib.util import name2index

class Driver(object):
    def __init__(self, name, mode=0, freq=None, spec=None):
        self.__mode = mode
        self.__name = name
        self.__freq = freq
        self.__spec = spec
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
    
    def get_profile(self):
        info = {'type':str(self), 'mode':self.__mode}
        if self.__freq:
            info.update({'freq':self.__freq})
        if self.__spec:
            info.update({'spec':self.__spec})
        return info
    
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
    