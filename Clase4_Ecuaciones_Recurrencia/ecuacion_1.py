"""
Ecuación 1
T(n) = 2T(n/2) + O(1)

Método: Maestro

a = 2
b = 2
d = 0

log_b(a) = log_2(2) = 1

Como d < log_b(a):
0 < 1

Caso 1 del método maestro:
T(n) = Θ(n^(log_b(a)))
T(n) = Θ(n)
"""

def recurrencia_1(n):
    if n <= 1:
        return 1
    return 2 * recurrencia_1(n // 2) + 1


if __name__ == "__main__":
    print("Ecuación 1: T(n) = 2T(n/2) + O(1)")
    print("Resultado teórico: Θ(n)")
    for n in [1, 2, 4, 8, 16, 32]:
        print(f"n = {n:2d} -> T(n) = {recurrencia_1(n)}")
