# util.py
#
# Copyright (C) 2016 Yi-Wei Ci
#
# Distributed under the terms of the MIT license.
#

def send(buf):
    try:
        print(str(buf))
    except:
        pass

def name2index(pin):
    val = int(pin[1:])
    if val >= 128:
        return
    if pin.startswith('X'):
        return val
    elif pin.startswith('Y'):
        return 128 + val
