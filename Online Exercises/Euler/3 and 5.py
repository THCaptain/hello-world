__author__ = 'thomas'

x=0
y=0
for i in range(1,1000):
    if i % 3 == 0:
        y = y + i
    elif i % 5 == 0:
        y = y + i
    else:
        y = y
        print 'NEXT'
print y