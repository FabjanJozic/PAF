A1 = int(input('Upiši vrijednost x koordinate prve točke: '))
A2 = int(input('Upiši vrijednost y koordinate prve točke: '))
B1 = int(input('Upiši vrijednost x koordinate druge točke: '))
B2 = int(input('Upiši vrijednost y koordinate prve točke: '))

k = (B2 - A2)/(B1 - A1)
a = -k*A1 + A2

if a <0:
    print('Jednadžba pravca kroz te dvije točke je  {}'.format('y='+str(k)+'x'+str(a)))
elif a >0:
    print('Jednadžba pravca kroz te dvije točke je  {}'.format('y='+str(k)+'x+'+str(a)))
else:
    print('Jednadžba pravca kroz te dvije točke je  {}'.format('y='+str(k)+'x'))

