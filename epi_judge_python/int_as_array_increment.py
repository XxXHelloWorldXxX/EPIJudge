from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    
    # We start adding values to numbers
    # from the right so thats what we do here
    cur_index = len(A) - 1

    # In case a number overlaps
    overlap = True

    while overlap:
        if cur_index < 0:
            # If we had a list like [9,9]
            # then we'd have to insert 1 
            # at the front of the list [1,0,0]
            A.insert(0, 1)
            overlap = False
            continue

        # Add plus one
        A[cur_index] += 1

        # If our value becomes 10,
        # then it overlaped
        if A[cur_index] == 10:
            overlap = True
            A[cur_index] = 0
            cur_index -= 1
            continue
        
        # We successfully added plus one
        else:
            overlap = False

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
