def Potencia(b,e):
    if e<0:
        exp= -e
    else:
        exp=e

    P=1
    for i in range(1,exp+1):
        P=P*b
        if e<0:
            P=1/P
    return P