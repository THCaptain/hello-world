__author__ = 'thomas'

x = 1
y = 2
z = 0
a = 0

while x < 4000001:
    z = x + y
    if y % 2 == 0:
        a = a + y
    x = y
    y = z

print a