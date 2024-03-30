def imprime_naturais(N):
    if N < 0:
        return 
    else:
        imprime_naturais(N-1)
        print(N)
n = int(input('Digite N: '))
print(imprime_naturais(n))
