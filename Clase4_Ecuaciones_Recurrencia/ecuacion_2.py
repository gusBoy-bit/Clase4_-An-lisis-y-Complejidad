"""
Ecuación 2
T(n) = 4T(n/2) + O(n)

Método: Maestro

a = 4
b = 2
d = 1

log_b(a) = log_2(4) = 2

Como d < log_b(a):
1 < 2

Caso 1 del método maestro:
T(n) = Θ(n^(log_b(a)))
T(n) = Θ(n^2)
"""

def recurrencia_2(n):
    if n <= 1:
        return 1
    return 4 * recurrencia_2(n // 2) + n


if __name__ == "__main__":
    print("Ecuación 2: T(n) = 4T(n/2) + O(n)")
    print("Resultado teórico: Θ(n²)")
    for n in [1, 2, 4, 8, 16, 32]:
        print(f"n = {n:2d} -> T(n) = {recurrencia_2(n)}")
