
def solution(h, q):
    nodes = 2 ** h - 1  # Total number of nodes in the perfect binary tree
    results = []

    for node_label in q:
        if node_label < 1 or node_label >= nodes:
            results.append(-1)  # Invalid node label
        else:
            parent = find_parent(node_label, nodes)
            results.append(parent)

    return results

def find_parent(node_label, nodes):
    if node_label == nodes:
        return -1  # The root has no parent

    left_child = node_label * 2
    right_child = node_label * 2 + 1

    if left_child >= nodes or right_child >= nodes:
        return -1  # Node has no children, so no parent

    if left_child < nodes and node_label != nodes:
        return left_child  # Left child is the parent of the current node

    if right_child < nodes and node_label != nodes:
        return right_child  # Right child is the parent of the current node


print(solution(3, [1, 4, 7]))