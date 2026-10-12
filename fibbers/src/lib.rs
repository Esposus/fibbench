use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod fibbers {
    use pyo3::prelude::*;

    /// Recursive fibonacci.
    #[pyfunction]
    fn fibrust(n: usize) -> usize {
        if n <= 1 {
            n
        } else {
            fibrust(n - 1) + fibrust(n - 2)
        }
        
    }
}
