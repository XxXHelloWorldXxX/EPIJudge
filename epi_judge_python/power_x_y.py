from test_framework import generic_test


def power(x: float, y: int) -> float:
    return x**y


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
