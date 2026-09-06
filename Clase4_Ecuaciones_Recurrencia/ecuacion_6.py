"""
Ecuación 6
T(n) = 3T(n/4) + O(n^2)

Método: Maestro

a = 3
b = 4
d = 2

log_b(a) = log_4(3) ≈ 0.792

Como:
2 > 0.792

corresponde al Caso 3 del método maestro.

T(n) = Θ(n^2)
"""

import math


def recurrencia_6(n):
    if n <= 1:
        return 1
    return 3 * recurrencia_6(n // 4) + n ** 2


if __name__ == "__main__":
    log_b_a = math.log(3, 4)

    print("Ecuación 6: T(n) = 3T(n/4) + O(n²)")
    print(f"log_4(3) = {log_b_a:.3f}")
    print("Resultado teórico: Θ(n²)")

    for n in [1, 4, 16, 64, 256]:
        print(f"n = {n:3d} -> T(n) = {recurrencia_6(n)}")
