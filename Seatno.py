import random
import string
def Seatno(x,y):
    return chr(random.randint(ord(x), ord(y)))
section=Seatno('A','Z')
no_=random.randint(00,100)
a=section,"-",no_

