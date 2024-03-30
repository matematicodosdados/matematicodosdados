def populacao(ha,ta,hb,tb):
    contador = 0 
    while ha < hb: 
        contador += 1 
        ha = ha + (ta/100)*ha 
        hb = hb + (tb/100)*hb 
    return contador
    


        