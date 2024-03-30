def imprime_naturais_pares(N):
    if N < 0:
        return 
    else:
        imprime_naturais_pares(N-1)
        if N%2 == 0:
            print(N)
n = int(input('Digite N: '))
print(imprime_naturais_pares(n))