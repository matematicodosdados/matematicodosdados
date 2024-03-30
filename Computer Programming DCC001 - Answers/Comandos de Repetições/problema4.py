n = float(input('Digite o preço do pão: '))
for i in range(1,51):
    print(str(i), '-', 'R$ %.2f' % float(n*i))