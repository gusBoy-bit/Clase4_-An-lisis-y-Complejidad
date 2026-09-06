"""
Ecuación 3
T(n) = 2T(n/2) + O(n^2)

Método: Maestro

a = 2
b = 2
d = 2

log_b(a) = log_2(2) = 1

Como d > log_b(a):
2 > 1

Caso 3 del método maestro:
T(n) = Θ(n^d)
T(n) = Θ(n^2)
"""

def recurrencia_3(n):
    if n <= 1:
        return 1
    return 2 * recurrencia_3(n // 2) + n ** 2


if __name__ == "__main__":
    print("Ecuación 3: T(n) = 2T(n/2) + O(n²)")
    print("Resultado teórico: Θ(n²)")
    for n in [1, 2, 4, 8, 16, 32]:
        print(f"n = {n:2d} -> T(n) = {recurrencia_3(n)}")
