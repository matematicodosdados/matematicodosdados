#solicita o raio da circunferência
raio_da_circunferência = float(input('Digite o valor do raio da circunferência: '))
pi = 3.1415
perimetro = 2*pi*raio_da_circunferência
area = pi*(raio_da_circunferência)**2
volume = 4*pi*(raio_da_circunferência**3)/3
print('Perímetro: %.2f ' % perimetro)
print('Área: %.2f' % area)
print('Volume: %.2f' % volume)