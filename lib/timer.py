# timer.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

TIMER_MAX = 11

_functions = {}
_timers = {'Y1':((8, 1),), 'Y2':((8, 2),), 'Y3':((4, 3), (10, 1)), 'Y4':((4, 4), (11, 1)), 'Y7':((12, 1),), 'Y8':((12, 2),), 'Y9':((2, 3),), 'Y10':((2, 4),), 'X1':((5, 1), (2, 1)), 'X2':((5, 2), (2, 2)), 'X3':((9, 1), (5, 3), (2, 3)), 'X4':((9, 2), (5, 4), (2, 4)), 'X6':((2, 1),), 'X7':((13, 1),), 'X8':((14, 1),), 'X9':((4, 1),), 'X10':((4, 2),)}

class Timer(object):
    def __init__(self):
        self._cnt = 0
        self._curr = {}
    
    def alloc(self, pin):
        if self._cnt >= TIMER_MAX:
            return
        
        timers = _timers.get(pin)
        if not timers:
            return
        
        curr = self._curr.get(pin)
        if curr:
            pos = len(curr)
            if pos == len(timers):
                return
            self._curr[pin].append(timers[pos])
        else:
            pos = 0
            self._curr.update({pin:[timers[pos]]})
        
        self._cnt += 1
        return timers[pos]

_timer = Timer()

def alloc(pin):
    return _timer.alloc(pin)

def _proc(name):
    func = _functions.get(name)
    func()
    
def _timer0(arg):
    _proc(0)

def _timer1(arg):
    _proc(1)

def _timer2(arg):
    _proc(2)

def _timer3(arg):
    _proc(3)

def _timer4(arg):
    _proc(4)

def _timer5(arg):
    _proc(5)

def _timer6(arg):
    _proc(6)

def _timer7(arg):
    _proc(7)

def _timer8(arg):
    _proc(8)

def _timer9(arg):
    _proc(9)

def _timer10(arg):
    _proc(10)


def register(pin, callback):
    n = len(_functions)
    if n == TIMER_MAX:
        return
    _functions.update({n:callback})
    if 0 == n:
        return _timer0
    elif 1 == n:
        return _timer1
    elif 2 == n:
        return _timer2
    elif 3 == n:
        return _timer3
    elif 4 == n:
        return _timer4
    elif 5 == n:
        return _timer5
    elif 6 == n:
        return _timer6
    elif 7 == n:
        return _timer7
    elif 8 == n:
        return _timer8
    elif 9 == n:
        return _timer9
    elif 10 == n:
        return _timer10
