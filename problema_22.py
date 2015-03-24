import string

def get_valor_nombre(nombre):
    """
    Devuelve la suma de los valores correspondientes a cada letra de la cadena nombre, siendo A=1, B=2, ..., Z=26
    """

    alfabeto = string.ascii_uppercase

    lista = []
    for letra in nombre:
        lista.append(alfabeto.index(letra) + 1)

    return sum(lista)

# Abro el archivo de nombres
with open('problema_22-nombres.txt', 'rb') as archivo_nombres:
    for linea in archivo_nombres:

        # Elimino las comillas dobles y paso la linea a una lista
        lista_nombres = linea.replace("\"", "").split(',')

        # Ordeno la lista alfabeticamente
        lista_nombres_ordenada = sorted(lista_nombres)

lista = []
for n in lista_nombres_ordenada:
    lista.append((lista_nombres_ordenada.index(n)+1) * get_valor_nombre(n))

print sum(lista)