#recebe um intero de 4 algarismo
numero = int(input('Digite um inteiro de 4 algarismos: '))
print('Valor invertido: %s' % str(int(numero%1000%100%10))+str(int((numero%1000%100 - numero%1000%100%10)/10))+str(int((numero%1000 - numero%1000%100)/100))+str(int((numero-numero%1000)/1000)))
