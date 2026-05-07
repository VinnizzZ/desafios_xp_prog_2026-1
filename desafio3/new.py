def processar(d, t):
    r = 0
    if t.upper() == 'VIP': 
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
    if isinstance(v, str):
        try:
            v = float(v)
            return 'R$' + f'{v:.2f}'
        except:
            "Valor inválido, impossível realizar conversão"
    return 'R$' + f'{v:.2f}'
    
print(formatar('20'))