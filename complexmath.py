class Complex:
    "Complex number definition"
    def __init__(self, real_part=0, imag_part=0):
        self.r = real_part
        self.i = imag_part
    def __str__(self):
        if self.r == 0 and self.i == 0:
            complex_str = str(0)
        elif self.r == 0 and self.i != 0:
            complex_str = str(self.i) + "i"
        elif self.i == 0 and self.r != 0:
            complex_str = str(self.r)
        elif self.i > 0:
            complex_str = str(self.r) + " + " + str(self.i) + "i"
        else:
            neg_im_pt = (-1) * self.i
            complex_str = str(self.r) + " - " + str(neg_im_pt) + "i"
        return complex_str
    
    def __add__(self, other):
        real_pt = self.r + other.r
        imag_pt = self.i + other.i
        return Complex(real_pt, imag_pt)
    
    def __sub__(self, other):
        real_pt = self.r - other.r
        imag_pt = self.i - other.i
        return Complex(real_pt, imag_pt)
    
    def __mul__(self, other):
        real_pt = (self.r * other.r) - (self.i * other.i)
        imag_pt = (self.r * other.i) + (self.i * other.r)
        return Complex(real_pt, imag_pt)


if __name__ == "__main__":
    x = Complex(2,-7.2)
    y = Complex(-9, 3.6)
    z = Complex(15.4,-8)
    
    print(x + y + z)
    print(sum([x,y,z]))