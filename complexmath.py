class Complex:
    "Complex number definition"
    def __init__(self, real_part=0, imag_part=0):
        self.re = real_part
        self.im = imag_part

    def __str__(self):
        if self.re == 0 and self.im == 0:
            complex_str = str(0)
        elif self.re == 0 and self.im != 0:
            complex_str = str(self.im) + "i"
        elif self.im == 0 and self.re != 0:
            complex_str = str(self.r)
        elif self.im > 0:
            complex_str = str(self.re) + " + " + str(self.im) + "i"
        else:
            neg_im_pt = (-1) * self.im
            complex_str = str(self.re) + " - " + str(neg_im_pt) + "i"
        return complex_str
    
    def __add__(self, other):
        real_pt = self.re + other.re
        imag_pt = self.im + other.im
        return Complex(real_pt, imag_pt)
    
    def __sub__(self, other):
        real_pt = self.re - other.re
        imag_pt = self.im - other.im
        return Complex(real_pt, imag_pt)
    
    def __mul__(self, other):
        real_pt = (self.re * other.re) - (self.im * other.im)
        imag_pt = (self.re * other.im) + (self.im * other.re)
        return Complex(real_pt, imag_pt)
    