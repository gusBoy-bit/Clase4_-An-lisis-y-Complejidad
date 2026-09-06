"""
Ecuación 4
T(n) = T(n-1) + O(1)

No se puede aplicar el método maestro porque el tamaño
del subproblema disminuye mediante una resta y no una división.

Método: Sustitución / Árbol de recursión

Desarrollo:
T(n) = T(n-1) + 1
     = T(n-2) + 1 + 1
     = T(n-3) + 3
     ...
     = T(1) + (n-1)

Por lo tanto:
T(n) = Θ(n)
"""

def recurrencia_4(n):
    if n <= 1:
        return 1
    return recurrencia_4(n - 1) + 1


if __name__ == "__main__":
    print("Ecuación 4: T(n) = T(n-1) + O(1)")
    print("Resultado teórico: Θ(n)")
    for n in [1, 2, 4, 8, 16, 32]:
        print(f"n = {n:2d} -> T(n) = {recurrencia_4(n)}")
