def tamanho_maior_string(lista):
    lista_1 = []
    if lista == []:
        return 0 
    else:
        for i in lista: 
            lista_1 += [len(i)]
        lista_1.sort()
        return max(lista_1)