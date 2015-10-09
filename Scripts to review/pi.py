from __future__ import with_statement #function from stackoverflow answers
import decimal                          # https://stackoverflow.com/questions/347734/gauss-legendre-algorithm-in-python

def pi_gauss_legendre():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                #
        pi = None                                               #
        while 1:                                                #formula from Gauss Legendre algorithm :
            an = (a + b) / 2                                    #https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
            b = (a * b).sqrt()                                  #
            t -= p * (a - an) * (a - an)                        #
            a, p = an, 2*p                                      #
            piold = pi                                          #
            pi = (a + b) * (a + b) / (4 * t)                    #
            if pi == piold:                                     # equal within given precision
                break                                           #
    return +pi
print "How many digits of Pi would you like to compute? (3000 max)\n ****************"
digits = input('*>')
if digits > 3000:
    print "TURN UP! This guy is crazy as fuck he's gotta be on molly or some powder or something"
    exit (0)
else:
    print "Coming right up, homie.....\n"
decimal.getcontext().prec = digits
print "Result:\n", pi_gauss_legendre()

