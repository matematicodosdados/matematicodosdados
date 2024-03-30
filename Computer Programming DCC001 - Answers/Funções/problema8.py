def estacionamento(h1,e1,h2,e2):
    tempo1 = (h2-h1)*60 +(e2-e1)
    horas = int(tempo1/60)
    minutos = tempo1%60
    return minutos
print(estacionamento(12,30,15,31))