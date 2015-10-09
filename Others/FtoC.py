def Celtofah(cel):
    Fah = (cel*1.8) + 32
    return Fah
def Fahtocel(Fah):
    Cel = (Fah - 32) / 1.8
    return Cel

x = 0
y = 0
a = 0

print "Enter the temperature to convert:"
x = input('>')
print "Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius"
y = input('>')

if y == 1:
    a = Celtofah(x)
    print "\n>>Celsius to Fahrenheit. \n %d C = %d F" % (x, a)
elif y == 2:
    a = Fahtocel(x)
    print "\n>>Fahrenheit to Celsius. \n %d F = %d C" % (x, a)
elif y != 1 or 2:
    print 'Invalid input, you doofus.'
    exit(0)
