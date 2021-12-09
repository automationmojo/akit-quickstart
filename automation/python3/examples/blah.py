import threading

class Blah:
    def __init__(self):
        self._a = 1
        self._b = 2
        self._c = threading.Event()
        self._c.clear()
        return
    
    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b

    @property
    def c(self):
        self._c.wait()
        return "success"

if __name__ == "__main__":
    blah = Blah()
    print("blah a={}".format(blah.a))   # Put Breakpoint Here
