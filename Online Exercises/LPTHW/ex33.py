numbers = []
def loopdidoop (a):
    i = 0
    while i < a+1:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


a1 = int(raw_input('>>>'))
print loopdidoop(a1)
print numbers