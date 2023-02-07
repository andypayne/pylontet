
def factorial_recur(n):
    if n <= 1:
        return 1
    return n * factorial_recur(n - 1)


def factorial_iter(n):
    if n <= 1:
        return 1
    i = n
    fact = 1
    while i > 1:
        fact *= i
        i -= 1
    return fact


def run_tests(fn):
    res = fn(0)
    assert res == 1
    res = fn(1)
    assert res == 1
    res = fn(2)
    assert res == 2
    res = fn(3)
    assert res == 6
    res = fn(4)
    assert res == 24 
    res = fn(5)
    assert res == 120
    res = fn(10)
    assert res == 3628800
    res = fn(100)
    assert res == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


if __name__ == "__main__":
    import timeit
    run_tests(factorial_recur)
    run_tests(factorial_iter)
    n = 950
    print(f"Running recursive factorial...")
    t_recur = timeit.timeit(lambda: factorial_recur(n), number=1000)
    print(f"Time: {t_recur / 1000}")
    print(f"Running iterative factorial...")
    t_iter = timeit.timeit(lambda: factorial_iter(n), number=1000)
    print(f"Time: {t_iter / 1000}")

