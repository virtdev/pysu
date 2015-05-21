class Event(object):
    def __init__(self):
        self._active = False
    
    def is_set(self):
        return self._active
    
    def clear(self):
        self._active = False
        
    def set(self):
        self._active = True
