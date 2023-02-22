

def permute(s):
    """
    Permute using recursion.
    """
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            new_perms = permute(s[:i] + s[i + 1:])
            perms += [c + perm for perm in new_perms]
        return perms


################################################################################

from math import factorial


def permute_iter(s):
    """
    Permute using iteration.
    """
    perms = []
    for n in range(factorial(len(s))):
        perm = ''
        for i in range(len(s)):
            perm += s[(i + n) % len(s)]
        perms.append(perm)
    return perms


################################################################################


if __name__ == "__main__":
    import timeit
    s = "abcdef"
    print(f"Running recursive permute...")
    t_recur = timeit.timeit(lambda: permute(s), number=1000)
    print(f"Time: {t_recur / 1000}")
    print(f"Running iterative permute...")
    t_iter = timeit.timeit(lambda: permute_iter(s), number=1000)
    print(f"Time: {t_iter / 1000}")
    if t_recur < t_iter:
        print(f"The recursive version wins by {(t_iter - t_recur) / 1000}.")
    elif t_iter < t_recur:
        print(f"The iterative version wins by {(t_recur - t_iter) / 1000}.")
    else:
        print("It's a tie.")

