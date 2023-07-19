from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    str_x = str(x)

    # Make sure that str_x exists
    if not str_x:
        return False

    length = len(str_x)
    # If it's just one number then
    # it's a palindrome
    if length == 1:
        return True

    if (length % 2) == 0:
        even = True
    else:
        even = False

    # Pointers
    start = 0
    end = length - 1


    if even:
        while True:
            if not str_x[start] == str_x[end]:
                return False
            
            start += 1
            if start == end:
                break
            end -= 1

    else:
        while True:
            if not str_x[start] == str_x[end]:
                return False
            
            start += 1
            end -= 1
            if start == end:
                break

    return True

    




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
