
def jednadzba_pravca():
    A1 = int(input('Upiši vrijednost x koordinate prve točke: '))
    A2 = int(input('Upiši vrijednost y koordinate prve točke: '))
    B1 = int(input('Upiši vrijednost x koordinate druge točke: '))
    B2 = int(input('Upiši vrijednost y koordinate druge točke: '))

    k = (B2 - A2)/(B1 - A1)
    a = -k*A1 + A2
    b = None

    if a <0:
        b = 'Jednadžba pravca kroz te dvije točke je  y='+str(k)+'x'+str(a)
    elif a >0:
        b = 'Jednadžba pravca kroz te dvije točke je  y='+str(k)+'x+'+str(a)
    else:
        b = 'Jednadžba pravca kroz te dvije točke je  y='+str(k)+'x'

    return b


print(jednadzba_pravca())