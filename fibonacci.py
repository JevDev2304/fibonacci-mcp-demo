"""
Algoritmo de Serie de Fibonacci
================================
Tres implementaciones con distintas ventajas:
  1. Recursiva con memoización  → elegante, O(n) tiempo/espacio
  2. Iterativa                  → eficiente, O(n) tiempo, O(1) espacio
  3. Generador                  → ideal para secuencias largas / lazy evaluation

Creado via protocolo MCP desde Claude Code  🤖
"""

from functools import lru_cache
from typing import Generator


# ─────────────────────────────────────────────
# 1. Recursiva con memoización
# ─────────────────────────────────────────────
@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """
    Retorna el n-ésimo número de Fibonacci usando recursión con caché.

    Args:
        n: posición en la serie (0-indexado)

    Returns:
        El n-ésimo número de Fibonacci.

    Raises:
        ValueError: si n es negativo.
    """
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ─────────────────────────────────────────────
# 2. Iterativa
# ─────────────────────────────────────────────
def fibonacci_iterative(n: int) -> int:
    """
    Retorna el n-ésimo número de Fibonacci de forma iterativa.
    Complejidad: O(n) tiempo, O(1) espacio.

    Args:
        n: posición en la serie (0-indexado)

    Returns:
        El n-ésimo número de Fibonacci.

    Raises:
        ValueError: si n es negativo.
    """
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# ─────────────────────────────────────────────
# 3. Generador (lazy evaluation)
# ─────────────────────────────────────────────
def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    Genera los primeros `limit` números de Fibonacci usando un generador.
    Ideal para procesar secuencias muy largas sin cargar todo en memoria.

    Args:
        limit: cantidad de números a generar.

    Yields:
        Números de Fibonacci en orden.
    """
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


# ─────────────────────────────────────────────
# Demo
# ─────────────────────────────────────────────
if __name__ == "__main__":
    N = 10

    print("=" * 45)
    print(f"  Serie de Fibonacci — primeros {N} términos")
    print("=" * 45)

    # Generador: imprime la serie completa
    serie = list(fibonacci_generator(N))
    print(f"\nSerie:      {serie}")

    # Comparación de los tres métodos para el término N-1
    idx = N - 1
    rec = fibonacci_recursive(idx)
    ite = fibonacci_iterative(idx)
    print(f"\nFib({idx}) recursiva:  {rec}")
    print(f"Fib({idx}) iterativa:  {ite}")
    print(f"Fib({idx}) generador:  {serie[idx]}")
    print("\nTodos los métodos coinciden:", rec == ite == serie[idx])
    print("=" * 45)
