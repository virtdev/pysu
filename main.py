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

__args = []
__kwargs = {}
__func = None
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
    if type(__args) == list and type(__kwargs) == dict:
        __ctrl.process(index, op, *__args, **__kwargs)

def test():
    __create()
    while(True):
        __ctrl.trig()
        __ctrl.poll()
        time.sleep(1)

def execute():
    try:
        if __func:
            if type(__kwargs) == dict:
                res = __func(**__kwargs)
                if res:
                    send(res)
    except:
        pass
