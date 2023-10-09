from typing import Dict, List, Set


"""
Connected components
"""


def num_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    Given the number of nodes (n) and a list of undirected edges (edges),
    return the number of connected components in the graph.
    Should this count isolated nodes not connected by any edges?
    """
    """
    - comps: a dictionary mapping a node to a set of other nodes connected to it
    - comp_dict: a dictionary 
    """
    comps: Dict[Set[int]] = {}
    comp_dict: Dict[int] = {}
    for (n1, n2) in edges:
        if n1 not in comps and n2 not in comps:
            if n1 in comp_dict:
                comps[comp_dict[n1]].add(n2)
                comp_dict[n2] = comp_dict[n1]
            elif n2 in comp_dict:
                comps[comp_dict[n2]].add(n1)
                comp_dict[n1] = comp_dict[n2]
            else:
                comps[n1] = set([n1, n2])
                comp_dict[n1] = n1
                comp_dict[n2] = n1
        elif n1 in comps:
            comps[n1].add(n2)
            comp_dict[n2] = n1
        else:
            comps[n2].add(n1)
            comp_dict[n1] = n2
    return len(comps)


################################################################################

test_cases = [
    (5, [[0, 1], [1, 2], [3, 4]], 2),
]


def run_tests(fn=num_connected_components):
    passed_tests = 0
    for i, (n, edges, sl) in enumerate(test_cases):
        res = fn(n, edges)
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


