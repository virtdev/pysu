import pyb

LOW = 0
HIGH = 1

def pulseIn(pin, value, timeout=100000, width=1000000):
    try:
        if value == LOW:
            v0 = 1
            v1 = 0
        elif value == HIGH:
            v0 = 0
            v1 = 1
        start = pyb.micros()
        while pin.value() == v0:
            if pyb.elapsed_micros(start) > timeout:
                return
        start = pyb.micros()
        while pin.value() == v1:
            if pyb.elapsed_micros(start) >= width:
                break
        return pyb.elapsed_micros(start)
    except:
        pass
