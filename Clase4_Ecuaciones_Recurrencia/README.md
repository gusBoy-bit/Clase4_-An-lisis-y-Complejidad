# Clase 4 - Ecuaciones de Recurrencia


## Importante sobre el enunciado

En el documento de ejercicios, algunas recurrencias aparecen con el término `+ O` sin que se vea el argumento completo.

Para poder implementar y analizar los ejercicios en Python se usan estas interpretaciones didácticas:

1. `T(n) = 2T(n/2) + O(1)`
2. `T(n) = 4T(n/2) + O(n)`
3. `T(n) = 2T(n/2) + O(n^2)`
4. `T(n) = T(n-1) + O(1)`
5. `T(n) = T(n/3) + T(2n/3) + O(n)`
6. `T(n) = 3T(n/4) + O(n^2)`

Las ecuaciones 1, 2, 4 y 5 deben confirmarse con el enunciado original si el docente indicó otro término.

## Métodos usados

La Clase 4 propone:

- **Método maestro** cuando la recurrencia tiene la forma  
  `T(n) = a·T(n/b) + O(n^d)`.
- **Árbol de recursión** o **sustitución** cuando no cumple esa forma.

## Resultados

| Ecuación | Método | Resultado |
|---|---|---|
| 1 | Maestro | `Θ(n)` |
| 2 | Maestro | `Θ(n²)` |
| 3 | Maestro | `Θ(n²)` |
| 4 | Árbol / Sustitución | `Θ(n)` |
| 5 | Árbol de recursión | `Θ(n log n)` |
| 6 | Maestro | `Θ(n²)` |

## Estructura

- `ecuacion_1.py`
- `ecuacion_2.py`
- `ecuacion_3.py`
- `ecuacion_4.py`
- `ecuacion_5.py`
- `ecuacion_6.py`
- `main.py`

## Ejecución

Ejecutar todos los ejercicios:

```bash
python main.py
```

O ejecutar uno por separado:

```bash
python ecuacion_1.py
```

## Objetivo

El código no intenta calcular tiempos reales de ejecución. Cuenta una unidad de trabajo por cada término no recursivo para observar cómo crece `T(n)` y relacionarlo con el análisis teórico.
