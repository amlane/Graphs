# Since we want to find the farthest parent, we'll be using DFS
# We only need to return the parent, not a path
# we only want to move towards parents

# (parent, child)
# If the starting_node is never a child return -1

from utils import Stack, Queue  # These may come in handy


def get_parents(ancestors, child):
    results = list()
    for item in ancestors:
        if child == item[1]:
            results.append(item[0])
    return results


def earliest_ancestor(ancestors, starting_node):
    child_list = set()
    for item in ancestors:
        child_list.add(item[1])
    if starting_node not in child_list:
        return -1
    else:
        q = Stack()
        q.push([starting_node])
        visited = set()
        while q.size() > 0:
            path = q.pop()
            n = path[-1]
            if n not in visited:
                visited.add(n)
            for parent in get_parents(ancestors, n):
                path_copy = path.copy()
                path_copy.append(parent)
                q.push(path_copy)
        return path[-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 1))  # 10
print(earliest_ancestor(ancestors, 2))  # -1
print(earliest_ancestor(ancestors, 3))  # 10
print(earliest_ancestor(ancestors, 11))  # -1
print(earliest_ancestor(ancestors, 5))  # 4
print(earliest_ancestor(ancestors, 7))  # 4
print(earliest_ancestor(ancestors, 8))  # 4
print(earliest_ancestor(ancestors, 9))  # 4
