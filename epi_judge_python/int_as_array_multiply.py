from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:

    # sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    # num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # result = [0] * (len(num1) + len(num2))
    # for i in reversed(range(len(num1))):
    #     for j in reversed(range(len(num2))):
    #         result[i + j + 1] += num1[i] * num2[j]
    #         result[i + j] += result[i + j + 1] // 10
    #         result[i + j + 1] %= 10

    # # Remove the leading zeroes
    # result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # return [sign * result[0]] + result[1:]

    str_num1 = "".join([str(num) for num in num1])
    str_num2 = "".join([str(num) for num in num2])
    
    # Calculate result
    int_result = int(str_num1) * int(str_num2)

    # Check if it's a negative int
    if int_result < 0:
        hyphen = True
    else:
        hyphen = False

    # Create our array
    array_result = [int(num) for num in str(int_result) if not num == "-"]
    
    # Put a hyphen before the first number
    if hyphen:
        array_result[0] = -abs(array_result[0])

    return array_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
