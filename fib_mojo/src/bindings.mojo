from fibonacci import fib_native
from std.python import PythonObject
from std.python.bindings import PythonModuleBuilder
from std.os import abort


@export
def PyInit__native() abi("C") -> PythonObject:
    try:
        var m = PythonModuleBuilder("_native")
        m.def_function[fibmojo]("fibmojo", docstring="Рекурсивная реализация функции Фибоначчи.")
        return m.finalize()
    except e:
        abort(String("Ошибка при создании модуля Mojo для Python:", e))



def fibmojo(py_obj: PythonObject) raises -> PythonObject:
    return fib_native(UInt(py=py_obj))