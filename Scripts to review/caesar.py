__author__ = 'thomas'

def getInput():
    print 'Input the message to be translated : \n~~~~~~~~~~~'
    return raw_input()
def getFactor():
    print 'Input the spaces to shift (+ if A>Z, - if Z>A):'
    return int(raw_input('>'))

message = getInput()
factor = getFactor()
resultraw = []

print 'Message to encrypt or decrypt: \n ************** \n', message

charlist = list(message)

for i in charlist:
    x = ord(i)
    if x == 32:
        x = 32 - factor
    if x < 97 :
        x = ord(i) - factor
    y = x + factor
    if y >= 123 :
        y = y - 26
    z = chr(y)
    resultraw.append(z)
result = ''.join(resultraw)

print 'Encrypted/Decrypted message: \n ************** \n', result