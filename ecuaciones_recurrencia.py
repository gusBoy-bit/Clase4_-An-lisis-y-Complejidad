# Ecuaciones de Recurrencia
# Clase 4 - Análisis y Complejidad


# Ecuación 1
# T(n) = 2T(n/2) + O(1)

# Método Maestro
# a = 2
# b = 2
# d = 0
# log2(2) = 1
# Como 0 < 1, corresponde al caso 1.
# Resultado: Θ(n)

def ecuacion_1(n):
    if n <= 1:
        return 1
    return ecuacion_1(n // 2) + ecuacion_1(n // 2)


# Ecuación 2
# T(n) = 4T(n/2) + O(1)

# Método Maestro
# a = 4
# b = 2
# d = 0
# log2(4) = 2
# Como 0 < 2, corresponde al caso 1.
# Resultado: Θ(n^2)

def ecuacion_2(n):
    if n <= 1:
        return 1
    return (
        ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
        + ecuacion_2(n // 2)
    )


# Ecuación 3
# T(n) = 2T(n/2) + O(n^2)

# Método Maestro
# a = 2
# b = 2
# d = 2
# log2(2) = 1
# Como 2 > 1, corresponde al caso 3.
# Resultado: Θ(n^2)

def ecuacion_3(n):
    if n <= 1:
        return 1
    trabajo = n ** 2
    return ecuacion_3(n // 2) + ecuacion_3(n // 2) + trabajo


# Ecuación 4
# T(n) = T(n-1) + O(1)

# Método de Sustitución
# T(n) = T(n-1) + 1
# T(n) = T(n-2) + 2
# T(n) = T(n-3) + 3
# ...
# T(n) = T(1) + (n-1)
# Resultado: Θ(n)

def ecuacion_4(n):
    if n <= 1:
        return 1
    return ecuacion_4(n - 1) + 1


# Ecuación 5
# T(n) = T(n/3) + T(2n/3) + O(1)

# Método: Árbol de Recursión
# No se aplica el Método Maestro porque
# los subproblemas tienen tamaños diferentes.
# n/3 + 2n/3 = n
# La cantidad total de trabajo crece linealmente.
# Resultado: Θ(n)

def ecuacion_5(n):
    if n <= 1:
        return 1

    parte_1 = max(1, n // 3)
    parte_2 = n - parte_1

    return ecuacion_5(parte_1) + ecuacion_5(parte_2)


# Ecuación 6
# T(n) = 3T(n/4) + O(n^2)

# Método Maestro
# a = 3
# b = 4
# d = 2
# log4(3) ≈ 0.79
# Como 2 > 0.79, corresponde al caso 3.
# Resultado: Θ(n^2)

def ecuacion_6(n):
    if n <= 1:
        return 1

    trabajo = n ** 2

    return (
        ecuacion_6(n // 4)
        + ecuacion_6(n // 4)
        + ecuacion_6(n // 4)
        + trabajo
    )


if __name__ == "__main__":
    n = 8

    print("Ecuación 1:", ecuacion_1(n))
    print("Ecuación 2:", ecuacion_2(n))
    print("Ecuación 3:", ecuacion_3(n))
    print("Ecuación 4:", ecuacion_4(n))
    print("Ecuación 5:", ecuacion_5(n))
    print("Ecuación 6:", ecuacion_6(n))
