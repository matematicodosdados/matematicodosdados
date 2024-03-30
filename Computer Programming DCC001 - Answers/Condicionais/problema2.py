velocidade_max = float(input('Digite o valor da velocidade máxima: '))
velocidade = float(input('Digite o valor da velocidade registrada: '))
if velocidade <= velocidade_max:
    print('Sem infração')
elif velocidade <= velocidade_max + velocidade_max*0.2: 
    print('Infração média')
elif velocidade > velocidade_max + velocidade_max*0.2 and velocidade <= velocidade_max*0.5 + velocidade_max: 
    print('Infração grave')
else:
    velocidade > velocidade_max + velocidade_max*0.5
    print('Infração Gravíssima')