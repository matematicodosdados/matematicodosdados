def quantidade_pares(inicio, fim):
    b = 0 
    for i in range(inicio,fim+1):
        if i%2 == 0:
            b += 1
    return 'Quantidade de números pares: %d' % b