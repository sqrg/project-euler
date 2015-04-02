lista = []
for n in range(1000000):
    # bin(n)[2:] omite los dos primeros caracteres de bin(n)
    if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]:
        lista.append(n)

print sum(lista)