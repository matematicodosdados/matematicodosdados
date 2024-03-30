def soma_divisores(n):
    c = 1
    d = 0 
    while c < n-1: 
        c += 1 
        if n%c == 0:
            d += c 
    return 'Resultado: %d' % int(d+1)
