def peso_ideal(altura, sexo):
    if sexo == "F":
        return float((62.1*altura) - 44.7)
    if sexo == 'M':
        return float((72.7*altura) - 58)