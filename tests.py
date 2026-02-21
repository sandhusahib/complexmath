import complexmath
import matplotlib.pyplot as plt

x = complexmath.Complex(2,-7.2)
y = complexmath.Complex(-9, 3.6)
z = complexmath.Complex(15.4,-8)

print(complexmath.Complex())
print(x*y-z)
print(sum([x,y,z],start=complexmath.Complex(0)))

print(x.mod)
print(x.arg)

X = [0,x.re]
Y = [0,x.im]
plt.plot(X,Y)
plt.show()