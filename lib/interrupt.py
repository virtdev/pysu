# interrupt.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import pyb

INTP_MAX = 16

_functions = {}

def _proc(name):
    func = _functions.get(name)
    func()
    
def _int0(arg):
    _proc(0)

def _int1(arg):
    _proc(1)

def _int2(arg):
    _proc(2)

def _int3(arg):
    _proc(3)

def _int4(arg):
    _proc(4)

def _int5(arg):
    _proc(5)

def _int6(arg):
    _proc(6)

def _int7(arg):
    _proc(7)
    
def _int8(arg):
    _proc(8)

def _int9(arg):
    _proc(9)

def _int10(arg):
    _proc(10)

def _int11(arg):
    _proc(11)

def _int12(arg):
    _proc(12)

def _int13(arg):
    _proc(13)
    
def _int14(arg):
    _proc(14)

def _int15(arg):
    _proc(15)

def register(callback):
    n = len(_functions)
    if n == INTP_MAX:
        return
    _functions.update({n:callback})
    if 0 == n:
        return _int0
    elif 1 == n:
        return _int1
    elif 2 == n:
        return _int2
    elif 3 == n:
        return _int3
    elif 4 == n:
        return _int4
    elif 5 == n:
        return _int5
    elif 6 == n:
        return _int6
    elif 7 == n:
        return _int7
    elif 8 == n:
        return _int8
    elif 9 == n:
        return _int9
    elif 10 == n:
        return _int10
    elif 11 == n:
        return _int11
    elif 12 == n:
        return _int12
    elif 13 == n:
        return _int13
    elif 14 == n:
        return _int14
    elif 15 == n:
        return _int15

def irq_rising(pin, callback, pull=pyb.Pin.PULL_NONE):
    func = register(callback)
    if func:
        return pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING, pull, func)

def irq_falling(pin, callback, pull=pyb.Pin.PULL_NONE):
    func = register(callback)
    if func:
        return pyb.ExtInt(pin, pyb.ExtInt.IRQ_FALLING , pull, func)

def irq_rising_falling(pin, callback, pull=pyb.Pin.PULL_NONE):
    func = register(callback)
    if func:
        return pyb.ExtInt(pin, pyb.ExtInt.IRQ_RISING_FALLING, pull, func)
