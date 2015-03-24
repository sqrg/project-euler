def get_collatz(n):
    """
    Devuelve la secuencia de Collatz correspondiente a n
    """

    lista = []
    lista.append(n)
    x = n
    while x > 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = (3 * x) + 1

        lista.append(x)

    return lista

lista = [0,]
for n in range(1000000):
    if len(get_collatz(n)) > len(lista):
        lista = get_collatz(n)

print lista