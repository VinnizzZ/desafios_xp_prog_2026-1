def processar(d, t):
    r = 0
    if t == 'VIP': 
        if d > 500: 
            r = d * .8 
        else: r = d * .9

    else:
        if d>500:
            r=d*.95
        else:
            r=d

    if r>1000:
            r=r-50

    return r

def formatar(v):
    return 'R$' + f'{v:.2f}'