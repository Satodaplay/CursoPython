

def chequear_3_cifras(lista):

    for n in lista:

        lista_3_cifras = []

        if n in range(100, 1000):
            lista_3_cifras(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([55, 99, 600])
print(resultado)