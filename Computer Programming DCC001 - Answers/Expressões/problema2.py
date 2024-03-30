#solicita valores
velocidade_inicial = float(input('Digite o valor da velocidade: '))
aceleracao = float(input('Digite o valor da aceleração: '))
tempo = float(input('Digite o valor do tempo: '))
velocidade_final = velocidade_inicial + aceleracao*tempo
deslocamento = velocidade_inicial*tempo + (aceleracao*tempo*tempo)/2
print('Velocidade final: %.2f' % velocidade_final)
print('Distância percorrida: %.2f' % deslocamento)