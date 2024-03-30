def soma(m,n):
    if m == n:
        return m
    elif n > m:
        return m + soma(m+1,n)
numero1 = int(input('Digite m: '))
numero2 = int(input('Digite n:'))
print(soma(numero1,numero2))
