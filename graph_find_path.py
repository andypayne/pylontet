"""
Find all or shortest paths in a graph.

Based on:
https://www.python.org/doc/essays/graphs/

adjacency list:
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
"""

################################################################################


def find_path(adj_list, start, end, path=[]):
    # Note: using `path += [start]` will not create a new path variable, so it
    # won't work here. I thought one was shorthand for the other, but that's
    # not the case.
    path = path + [start]
    if start == end:
        return path
    if start not in adj_list:
        return None
    for node in adj_list[start]:
        if node not in path:
            new_path = find_path(adj_list, node, end, path)
            if new_path:
                return new_path
    return None


def find_all_paths(adj_list: dict, start: str, end: str, path: list=[]) -> list:
    path = path + [start]
    if start == end:
        return [path]
    if start not in adj_list:
        return []
    all_paths = []
    for node in adj_list[start]:
        if node not in path:
            new_paths = find_all_paths(adj_list, node, end, path)
            [all_paths.append(p) for p in new_paths]
    return all_paths



# This visits n + (n - 1) + (n - 2) + ... + 1 = n * (n - 1) nodes, so its
# time complexity is O(n^2).
def find_shortest_path(adj_list, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in adj_list:
        return None
    min_path = None
    for node in adj_list[start]:
        if node not in path:
            new_path = find_shortest_path(adj_list, node, end, path)
            # less than or equal to get the last minimal path, which is what is
            # in the test case.
            if (
                min_path is None
                or (
                    new_path is not None
                    and len(new_path) <= len(min_path)
                )
            ):
                min_path = new_path
    return min_path


################################################################################

from collections import deque 
from typing import Iterable 


def deep_flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in deep_flatten(x):
                yield sub_x
        else:
            yield x


def find_shortest_path_bfs(adj_list, start, end):
    dist = {start: [start]}    
    q = deque(start)
    while len(q) > 0:
        node = q.popleft()
        for next in adj_list[node]:
            if next not in dist:
                dist[next] = [dist[node], next]
                q.append(next)
    #return dist.get(end)
    return list(deep_flatten(dist.get(end)))


################################################################################

test_cases = [
    (
        {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        },
        'A',
        'D',
        ['A', 'C', 'D'],
     ),
]


def run_tests(fn=find_shortest_path):
    passed_tests = 0
    for i, (adj_list, start, end, sl) in enumerate(test_cases):
        res = fn(adj_list, start, end)
        if res == sl:
            passed_tests += 1
        else:
            print(f"#[{i}]: WRONG")
            print(f"Expected: {sl}, but got: {res}")
            break
    print(f"Passed {passed_tests} of {len(test_cases)} tests.")


################################################################################


if __name__ == "__main__":
    run_tests()


