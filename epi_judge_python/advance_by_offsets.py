from typing import List

from test_framework import generic_test

# def can_advance_to_end(A, parent_index, avaliable_steps, end):
#     possible_steps = range(1, avaliable_steps + 1)
#     for steps in possible_steps[::-1]:
#         # If we can reach the end
#         current_index = parent_index + steps
#         if current_index >= end:
#             return True
        
#         # If that field we are at 
#         # doesn't allow us to continue
#         elif A[current_index] == 0:
#             continue

#         # We found another path
#         # so we'll check if we can 
#         # advance to the end here
#         elif can_advance_to_end(A, current_index, A[current_index], end):
#             return True
        
#         # This route didn't work.
#         # Let's try walking more 
#         # steps, if we're allowed
#         else: continue
#     return False
            
def can_reach_end(A: List[int]) -> bool:

    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index




    # end = len(A) - 1

    # # If the board is one field big
    # # then you are already at the finish
    # if end == 0: 
    #     return True
    
    # # Where we currently are with 
    # # the steps that we took
    # parent_index = 0

    # # These are our avaliable steps
    # avaliable_steps = A[parent_index]
    
    # # If the first number is a 0 
    # # Then this game can't be won
    # if avaliable_steps == 0:
    #     return False
    
    # if can_advance_to_end(A, parent_index, avaliable_steps, end):
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
