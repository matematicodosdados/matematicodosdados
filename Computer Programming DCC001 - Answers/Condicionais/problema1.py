num1 = int(input('Digite o primeiro inteiro: '))
num2 = int(input('Digite o segundo inteiro: '))
num3 = int(input('Digite o terceiro inteiro: '))
num4 = int(input('Digite o quarto inteiro: '))
num5 = int(input('Digite o quinto inteiro: '))
x = 0 
if num1%3 == 0:
    x = x+1 
if num2%3 == 0:
    x = x+1 
if num3%3 == 0:
    x = x+1
if num4%3 == 0:
    x = x + 1
if num5%3 == 0:
    x = x + 1
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5: 
    print('Maior: %d' % num1)
    if num2 <= num3 and num2 <= num4 and num2 <= num1 and num2 <= num5: 
        print('Menor: %d' % num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5: 
        print('Menor: %d' % num3)
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5: 
        print('Menor: %d' % num4)
    elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4: 
        print('Menor: %d' % num5)
elif num2 >= num3 and num2 >= num4 and num2 >= num1 and num2 >= num5: 
    print('Maior: %d' % num2)
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5: 
        print('Menor: %d' % num1)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5: 
        print('Menor: %d' % num3)
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5: 
        print('Menor: %d' % num4)
    elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4: 
        print('Menor: %d' % num5)
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5: 
    print('Maior: %d' % num3)
    if num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5: 
        print('Menor: %d' % num4)
    elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4: 
        print('Menor: %d' % num5)
    elif num2 <= num3 and num2 <=num4 and num2 <= num1 and num2 <= num5: 
        print('Menor: %d' % num2)
    elif num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5: 
        print('Menor: %d' % num1)
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5: 
    print('Maior: %d' % num4)
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5: 
        print('Menor: %d' % num1)
    elif num2 <= num3 and num2 <= num4 and num2 <= num1 and num2 <= num5: 
        print('Menor: %d' % num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5: 
        print('Menor: %d' % num3) 
    elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4: 
        print('Menor: %d' % num5)  
elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4: 
    print('Maior: %d' % num5)
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5: 
        print('Menor: %d' % num1)
    elif num2 <= num3 and num2 <= num4 and num2 <= num1 and num2 <= num5: 
        print('Menor: %d' % num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5: 
        print('Menor: %d' % num3)
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5: 
        print('Menor: %d' % num4)
print('Quantidade de divisíveis por 3: %d' % x) 