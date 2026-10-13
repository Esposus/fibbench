def fib_native(n: UInt) -> UInt:
    if n <= 1:
        return n
    return fib_native(n - 1) + fib_native(n - 2)
