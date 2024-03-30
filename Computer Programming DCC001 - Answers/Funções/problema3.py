def pagamento(salario):
    if salario <= 280: 
        return float(salario + salario*0.2)
    elif salario > 280 and salario <= 700:
        return float(salario + salario*0.15)
    elif salario > 700 and salario <= 1500:
        return float(salario + salario*0.1)
    else:
        return float(salario + salario*0.05)