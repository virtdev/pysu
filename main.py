import time
from lib.util import send
from devices import devices
from dev.controller import Controller

__func = None
__args = None
__ctrl = Controller()

def create():
    for item in devices:
        try:
            exec('from drivers.%s import %s' % (item.lower(), item))
            pin = devices[item]
            if type(pin) == str:
                exec("__ctrl.add(%s('%s'))" % (item, pin))
            elif type(pin) == tuple:
                exec("__ctrl.add(%s%s)" % (item, str(pin)))
        except:
            pass

def setup():
    create()
    __ctrl.setup()

def mount():
    __ctrl.mount()

def process(index, op):
    __ctrl.process(index, op, __args)

def test():
    setup()
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
