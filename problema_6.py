def suma_cuadrados(n):
    """
    Devuelve la suma de los cuadrados de los primeros n numeros naturales, sin incluir el cero
    """

    lista = [n**2 for n in range(1,n+1)]
    return sum(lista)

def cuadrado_sumas(n):
    """
    Devuelve el cuadrado de la suma de los primeros n numeros naturales, sin incluir el cero
    """

    return sum(range(1,n+1))**2

print cuadrado_sumas(100) - suma_cuadrados(100)