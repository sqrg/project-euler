def es_multiplo_de(n, m):
    """
    Devuelve True si n es multiplo de m
    """

    return n%m ==  0

lista = []
for n in range(1000):
    if es_multiplo_de(n,3) or es_multiplo_de(n, 5):
        lista.append(n)

print sum(lista)