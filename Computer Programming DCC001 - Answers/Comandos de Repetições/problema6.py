numero = int(input('Digite um inteiro n: '))
a = 1 
b = 1 
c = 0
for i in range(2,numero): 
    c = a + b 
    a = b 
    b = c 
print(c)
    
        