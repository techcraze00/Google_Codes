

def solution(h, q):
    tree_size = 2 ** h - 1  # Total number of nodes in the perfect binary tree
    result = []

    for value in q:
        if value < 1 or value > tree_size:
            result.append(-1)  # Invalid converter value
        else:
            parent = tree_size
            offset = 2 ** (h - 1)  # Offset for finding the parent

            while offset > 0:
                left_child = parent - offset
                right_child = parent - 1

                if value == left_child or value == right_child:
                    result.append(parent)
                    break

                if value < left_child:
                    parent = left_child
                else:
                    parent = right_child

                offset //= 2
            else:
                result.append(-1)  # No parent found

    return result