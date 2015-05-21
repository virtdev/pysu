def send(buf):
    try:
        print(str(buf))
    except:
        pass

def pin2index(pin):
    val = int(pin[1:])
    if val >= 128:
        return
    if pin.startswith('X'):
        return val
    elif pin.startswith('Y'):
        return 128 + val
