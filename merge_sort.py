# Merge Sort
# Algoritmo Divide y Vencerás
#
# Recurrencia:
# T(n) = 2T(n/2) + O(n)
#
# Complejidad:
# Θ(n log n)


def ordenar_por_mezcla(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    # Divide
    medio = len(arreglo) // 2
    izquierda = arreglo[:medio]
    derecha = arreglo[medio:]

    # Vencerás
    izquierda = ordenar_por_mezcla(izquierda)
    derecha = ordenar_por_mezcla(derecha)

    # Combina
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado
