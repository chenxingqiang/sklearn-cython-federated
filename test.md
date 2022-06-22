`$ ipython `                                                                                                  15:07:43
Python 2.7.12 (default, Oct 11 2016, 05:20:59)
Type "copyright", "credits" or "license" for more information.

IPython 4.0.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.

%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

`In [1]: import numpy as np`
`In [2]: import dot_python`
`In [3]: import dot_cython`
`In [4]: a = np.random.randn(100, 200).astype(np.float32)`
`In [5]: b = np.random.randn(200, 50).astype(np.float32)`

`In [6]: %timeit -n 100 -r 3 dot_python.naive_dot(a, b)`
100 loops, best of 3: 560 ms per loop

`In [7]: %timeit -n 100 -r 3 dot_cython.naive_dot(a, b)`
100 loops, best of 3: 982 µs per loop

`In [8]: %timeit -n 100 -r 3 np.dot(a, b)`
`100 loops, best of 3: 49.2 µs per loop`
