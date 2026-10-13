# fibbench


### Создать виртуальное окрежение Python
```python
uv sync
```

### Скомпилировать Mojo
```bash
uv run mojo build fib_mojo/src/bindings.mojo -I fib_mojo/src --emit shared-lib -o fib_mojo/_native.so
```

### Скомпилировать Rust
```bash
cd fibbers && maturin develop --release && cd ..
```

### Запустить
```python
uv run main.py 20
```

### Ожидаемый вывод примерно такой
```bash
Fibonacci от 20 равно: 6765

Python μs per call: 971.223 μs
Python ms per call: 0.971 ms

Rust μs per call: 18.718 μs
Rust ms per call: 0.019 ms

Mojo μs per call: 15.595 μs
Mojo ms per call: 0.016 ms
```