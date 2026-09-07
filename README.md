# Clase 4 - Ecuaciones de Recurrencia

Trabajo práctico de ecuaciones de recurrencia y algoritmo Divide y Vencerás.

## Archivos

- `ecuaciones_recurrencia.py`
- `merge_sort.py`
- `main.py`

## Algoritmo investigado

Se utilizó Merge Sort como ejemplo de Divide y Vencerás.

Divide el arreglo en dos partes, ordena cada mitad de forma recursiva y luego combina los resultados.

Recurrencia:

`T(n) = 2T(n/2) + O(n)`

Complejidad:

`Θ(n log n)`

## Ejecución

Para probar las ecuaciones:

```bash
python ecuaciones_recurrencia.py
```

Para probar Merge Sort:

```bash
python main.py
```
