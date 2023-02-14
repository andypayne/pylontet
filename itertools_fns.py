import itertools


################################################################################
# accumulate
# Returns an iterator that performs the accumulated results of applying `func`
# (sum by default) to the elements of a list.

list(itertools.accumulate([10, 20, 30, 40]))
# [10, 30, 60, 100]

# running minimum
list(itertools.accumulate([100, 34, 56, 22, 8, 97, 54], func=min))
# [100, 34, 34, 22, 8, 8, 8]

list(itertools.accumulate([100, 40, 20], func=lambda x, y: x / y))
# [100, 2.5, 0.125]


################################################################################
# starmap
# Apply a function to an iterable using arguments/shape from the iterable.

arr = [(i, i // 2) for i in range(3, 10)]
# [(3, 1), (4, 2), (5, 2), (6, 3), (7, 3), (8, 4), (9, 4)]

list(itertools.starmap(lambda x, y: x**y, arr))
# [3, 16, 25, 216, 343, 4096, 6561]


################################################################################
# takewhile and dropwhile
# Similar to takeWhile in haskell or take-while in scheme, return the longest
# initial list of elements for which the predicate is true.

arr = (
    [i for i in range(20) if i % 2 == 1]
    + [4]
    + [i for i in range(21, 30) if i % 2 == 1]
)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 21, 23, 25, 27, 29]

list(itertools.takewhile(lambda x: x % 2 == 1, arr))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

list(itertools.dropwhile(lambda x: x % 2 == 1, arr))
# [4, 21, 23, 25, 27, 29]


################################################################################
# chain
# Return elements from each list sequentially until exhausted.

list(itertools.chain([1, 2, 3], [4, 5, 6]))
# [1, 2, 3, 4, 5, 6]

list(itertools.chain('abcd', 'efgh'))
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


################################################################################
# cycle
# Exhaust and repeat an iterable indefinitely.

it = itertools.cycle([8, 13, 21, 34])
[next(it) for _ in range(10)]
# [8, 13, 21, 34, 8, 13, 21, 34, 8, 13]


################################################################################
# compress
# Return elements from a list for which the corresponding items from a second
# list evaluate to True.

list(itertools.compress([1, 2, 3, 4], [1, 0, 1, 1]))
# [1, 3, 4]

list(itertools.compress("abcdefghi", [0, 1, 0, 1, 1]))
# ['b', 'd', 'e']

list(itertools.compress("abcdefghi", [False, True, True, False, True, True]))
# ['b', 'c', 'e', 'f']


################################################################################
# pairwise (python >= 3.10)
# Return each sequential pair of elements from a list.

list(itertools.pairwise('ZYXWVUTSR'))
# [('Z', 'Y'), ('Y', 'X'), ('X', 'W'), ('W', 'V'), ('V', 'U'), ('U', 'T'),
#  ('T', 'S'), ('S', 'R')]

list(itertools.starmap(lambda x, y: x**y, itertools.pairwise([1, 2, 3, 4])))
# [1, 8, 81]


################################################################################
# permutations
# Return all permutations of length `r` from a list, with no repeated elements.
# If `r` is not specified, it defaults to the length of the provided list. As a
# reminder, the number of permutations of length `r` of a collection of
# elements of length `n` is `n!/(n - r)!`.
# https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n

[''.join(ls) for ls in itertools.permutations('abc')]
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

list(itertools.permutations([12, 34, 56]))
# [(12, 34, 56), (12, 56, 34), (34, 12, 56), (34, 56, 12), (56, 12, 34),
#  (56, 34, 12)]

[''.join(ls) for ls in itertools.permutations('abcde', r=2)]
# ['ab', 'ac', 'ad', 'ae', 'ba', 'bc', 'bd', 'be', 'ca', 'cb', 'cd', 'ce',
#  'da', 'db', 'dc', 'de', 'ea', 'eb', 'ec', 'ed']

# Note - elements are considered unique based on their positions, not on their
# values.
list(itertools.permutations([1, 1, 1]))
# [(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1)]


################################################################################
# combinations
# Return all combinations of length `r` from a list.

list(itertools.combinations([10, 20, 30], 2))
# [(10, 20), (10, 30), (20, 30)]

[''.join(s) for s in itertools.combinations('abcd', 3)]
# ['abc', 'abd', 'acd', 'bcd']


################################################################################
# product
# Return the cartesian product of two or more input iterables, with an optional
# number of repetitions `repeat`.

[''.join(ls) for ls in itertools.product('abc', 'def')]
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

[''.join(ls) for ls in itertools.product('ab', 'cd', 'ef')]
# ['ace', 'acf', 'ade', 'adf', 'bce', 'bcf', 'bde', 'bdf']

list(itertools.product([1, 2], [3, 4, 5]))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]

list(itertools.product([1, 2], repeat=3))
# [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1),
#  (2, 2, 2)]


################################################################################
# repeat
# Repeat the input indefinitely (default), or `times` times, if supplied.

list(itertools.repeat(3, times=5))
# [3, 3, 3, 3, 3]

# repeat can be used to supply a constant parameter to a function used with map:
list(map(lambda x, y: x + y, [1, 2, 3], itertools.repeat(10)))
# [11, 12, 13]


################################################################################
# islice
# Slice an iterable with start/stop/step.

list(itertools.islice([n for n in range(30)], 9, 26, 3))
# [9, 12, 15, 18, 21, 24]


################################################################################
# groupby
# Group sequential elements from a list into groups based on an optional key.

[list(g) for _, g in itertools.groupby([1, 1, 1, 2, 4, 4, 4, 4, 5, 5, 6, 6])]
# [[1, 1, 1], [2], [4, 4, 4, 4], [5, 5], [6, 6]]


################################################################################

