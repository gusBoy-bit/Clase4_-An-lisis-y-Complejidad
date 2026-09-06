"""
Ecuación 5
T(n) = T(n/3) + T(2n/3) + O(n)

No tiene la forma exacta del método maestro porque los
dos subproblemas poseen tamaños diferentes.

Método: Árbol de recursión

En cada nivel, la suma de los tamaños de los subproblemas es n:

nivel 0:              n
                    /   \
nivel 1:          n/3   2n/3

La suma del trabajo de cada nivel es O(n).

La profundidad del árbol es O(log n), porque en cada llamada
el subproblema más grande se reduce aproximadamente por un
factor de 2/3.

Costo total:
O(n) * O(log n) = O(n log n)

Resultado:
T(n) = Θ(n log n)
"""

def recurrencia_5(n):
    if n <= 1:
        return 1

    izquierda = max(1, n // 3)
    derecha = n - izquierda

    return recurrencia_5(izquierda) + recurrencia_5(derecha) + n


if __name__ == "__main__":
    print("Ecuación 5: T(n) = T(n/3) + T(2n/3) + O(n)")
    print("Resultado teórico: Θ(n log n)")
    for n in [1, 3, 9, 27, 81, 243]:
        print(f"n = {n:3d} -> T(n) = {recurrencia_5(n)}")
