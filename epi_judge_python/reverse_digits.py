from test_framework import generic_test


def reverse(x: int) -> int:
    str_x = str(x)
    possible_hyphen = ""
    if "-" in str_x:
        str_x = str_x.replace("-", "")
        possible_hyphen = "-"
    backwards_x = str_x[::-1]
    return(int(possible_hyphen + backwards_x))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
