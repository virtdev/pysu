# main.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

import time
from lib.util import send
from conf.pysu import devices
from dev.controller import Controller

__func = None
__args = None
__active = False
__ctrl = Controller()

def __create():
    for item in devices:
        try:
            exec('from drivers.%s import %s' % (item.lower(), item))
            name = devices[item]
            if type(name) == str:
                exec("__ctrl.add(%s('%s'))" % (item, name))
            elif type(name) == tuple:
                exec("__ctrl.add(%s%s)" % (item, str(name)))
        except:
            pass

def mount():
    global __active
    
    if not __active:
        __active = True
        __create()
    __ctrl.mount()

def process(index, op):
    __ctrl.process(index, op, __args)

def test():
    __create()
    while(True):
        __ctrl.trig()
        __ctrl.poll()
        time.sleep(1)

def execute():
    try:
        if __func:
            res = __func(__args)
            if res:
                send(res)
    except:
        pass
