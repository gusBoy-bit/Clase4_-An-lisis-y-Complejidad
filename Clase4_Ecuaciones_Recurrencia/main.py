from ecuacion_1 import recurrencia_1
from ecuacion_2 import recurrencia_2
from ecuacion_3 import recurrencia_3
from ecuacion_4 import recurrencia_4
from ecuacion_5 import recurrencia_5
from ecuacion_6 import recurrencia_6


def mostrar(titulo, funcion, valores, resultado):
    print("\n" + "=" * 60)
    print(titulo)
    print("Resultado teórico:", resultado)
    print("-" * 60)

    for n in valores:
        print(f"n = {n:4d} -> T(n) = {funcion(n)}")


def main():
    mostrar(
        "Ecuación 1: T(n) = 2T(n/2) + O(1)",
        recurrencia_1,
        [1, 2, 4, 8, 16, 32],
        "Θ(n)"
    )

    mostrar(
        "Ecuación 2: T(n) = 4T(n/2) + O(n)",
        recurrencia_2,
        [1, 2, 4, 8, 16, 32],
        "Θ(n²)"
    )

    mostrar(
        "Ecuación 3: T(n) = 2T(n/2) + O(n²)",
        recurrencia_3,
        [1, 2, 4, 8, 16, 32],
        "Θ(n²)"
    )

    mostrar(
        "Ecuación 4: T(n) = T(n-1) + O(1)",
        recurrencia_4,
        [1, 2, 4, 8, 16, 32],
        "Θ(n)"
    )

    mostrar(
        "Ecuación 5: T(n) = T(n/3) + T(2n/3) + O(n)",
        recurrencia_5,
        [1, 3, 9, 27, 81],
        "Θ(n log n)"
    )

    mostrar(
        "Ecuación 6: T(n) = 3T(n/4) + O(n²)",
        recurrencia_6,
        [1, 4, 16, 64, 256],
        "Θ(n²)"
    )


if __name__ == "__main__":
    main()
