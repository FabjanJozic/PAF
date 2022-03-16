
def jednadzba_pravca(A1, A2, B1, B2):
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


print(jednadzba_pravca(1,4,2,7))