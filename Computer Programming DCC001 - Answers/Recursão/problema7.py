def imprime_naturais_impares(N):
    if N == 1:
        return print(1)
    else:
        if N%2 != 0:
            print(N)
        return imprime_naturais_impares(N-1)
n = int(input('Digite N: '))
print(imprime_naturais_impares(n))