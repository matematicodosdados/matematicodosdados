#recebe o tempo em segundos
tempo = float(input('Digite o valor do tempo: '))
print('Valor convertido:  %d' % int(tempo/3600), 'h', int(tempo%3600/60), 'min', int((tempo%3600)%60), 's') 