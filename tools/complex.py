import math

class complex(object):
    """description of class"""
    def __init__(self, real = 0.0, imag = 0.0):
        self.real = real
        self.imag = imag

    def get_real(self):
        return self._real
    def set_real(self, value):
        self._real = value

    def get_imag(self):
        return self._imag
    def set_imag(self, value):
        self._imag = value

    def get_mod(self):
        return math.sqrt(math.pow(self.real,2) + math.pow(self.imag,2))
    def set_mod(self, value):
        a = self.arg
        self.real = value * math.cos(a)
        self.imag = value * math.sin(a)

    def get_arg(self):
        return math.atan2(self.imag, self.real)
    def set_arg(self, value):
        m = self.mod
        self.real = m * math.cos(value)
        self.imag = m * math.sin(value)

    real = property(get_real, set_real)
    imag = property(get_imag, set_imag)
    mod = property(get_mod, set_mod)
    arg = property(get_arg, set_arg)
    
    def __str__(self):
        return "[" +  str(self.real) + "," + str(self.imag) + "]"

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
         return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __div__(self, other):
        d = other.real * other.real + other.imag * other.imag
        res = self * complex(other.real, - other.imag)
        res.real /= d
        res.imag /= d
        return res
        

