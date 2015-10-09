<<<<<<< HEAD
from __future__ import division

=======
>>>>>>> b1798038cbfdae99b0765ed1202cd0f2089e8a5a
def Celtofah(cel):
    Fah = (cel*1.8) + 32.0
    return Fah
def Fahtocel(Fah):
    Cel = (Fah - 32.0) / 1.8
    return Cel

x = 0
y = 0
a = 0

print "Enter the temperature to convert:"
x = float(input('>'))
print "Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius"
y = float(input('>'))

if y == 1:
    a = Celtofah(x)
    print "\n>>Celsius to Fahrenheit. \n %f C = %f F" % (x, a)
elif y == 2:
    a = Fahtocel(x)
    print "\n>>Fahrenheit to Celsius. \n %f F = %f C" % (x, a)
elif y != 1 or 2:
    print 'Invalid input, you doofus.'
    exit(0)
