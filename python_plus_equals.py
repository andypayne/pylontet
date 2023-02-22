"""
I thought `x += y` was shorthand for `x = x + y`, but that isn't completely
true.

This is a demonstration.
"""

def fn(a=[]):
    a += [123]
    return a


def fn2(a=[]):
    a = a + [123]
    return a


"""
# Sample use:

# With fn:
>>> arr = [10, 20, 30]
>>> fn(arr)
[10, 20, 30, 123]
>>> arr
[10, 20, 30, 123]

# Notice that arr has been modified.

>>> fn(arr)
[10, 20, 30, 123, 123]
>>> arr
[10, 20, 30, 123, 123]

# Now with fn2:
>>> arr = [10, 20, 30]
>>> fn2(arr)
[10, 20, 30, 123]
>>> arr
[10, 20, 30]

# arr is not modified by fn2, because `a = a + [123]` does not modify `a`, but
# creates a new variable.

>>> fn2(arr)
[10, 20, 30, 123]
>>> fn2(arr)
[10, 20, 30, 123]
>>> arr
[10, 20, 30]

"""

"""

The `+=` operator is implemented for objects by implementing the
[`__iadd__`](https://docs.python.org/3/reference/datamodel.html#object.__iadd__)
method.

```
    __iadd__(self, value, /):
        ...
```

In contrast, the `+` operator is implemented with the
[`__add__`](https://docs.python.org/3/reference/datamodel.html#object.__add__)
method.

Also see this discussion:
https://stackoverflow.com/questions/9766387/different-behaviour-for-list-iadd-and-list-add

"""

if __name__ == "__main__":
    arr = [10, 20, 30]
    fn(arr)
    assert arr == [10, 20, 30, 123]
    arr = [10, 20, 30]
    fn2(arr)
    assert arr == [10, 20, 30]


