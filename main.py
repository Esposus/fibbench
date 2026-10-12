import sys
from timeit import timeit


from fib_mojo import fibmojo

from src.fibbench.fibonacci import fib
from fibbers import fibrust

RUNS=100


def main():
    n = int(sys.argv[1])
    print(f"Fibonacci от {n} равно: {fibmojo(n)}")

    python_time_per_call = timeit(lambda: fib(n), number=RUNS) / RUNS
    print(f"\nPython μs per call: {python_time_per_call * 1_000_000:.3f} μs")
    print(f"Python ms per call: {python_time_per_call * 1_000:.3f} ms")

    rust_time_per_call = timeit(lambda: fibrust(n), number=RUNS) / RUNS
    print(f"\nRust μs per call: {rust_time_per_call * 1_000_000:.3f} μs")
    print(f"Rust ms per call: {rust_time_per_call * 1_000:.3f} ms")

    mojo_time_per_call = timeit(lambda: fibmojo(n), number=RUNS) / RUNS
    print(f"\nMojo μs per call: {mojo_time_per_call * 1_000_000:.3f} μs")
    print(f"Mojo ms per call: {mojo_time_per_call * 1_000:.3f} ms")


if __name__ == "__main__":
    main()