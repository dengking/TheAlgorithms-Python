# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 11:21
# @File    : Euclidean_algorithm


def recursive_gcd(a, b):
    """
    gcd(a, b) = gcd(b, a mode b)
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    remainder = a % b
    if remainder == 0:
        return b
    return recursive_gcd(b, remainder)


def iterative_gcd(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    while True:
        if b == 0:
            return a
        remainder = a % b
        if remainder == 0:
            return b
        a, b = b, remainder


if __name__ == '__main__':
    print(recursive_gcd(2, 4))
    print(iterative_gcd(2, 4))
    assert recursive_gcd(2, 4) == recursive_gcd(4, 2) == iterative_gcd(2, 4) == iterative_gcd(4, 2)
    print(recursive_gcd(1997, 615))
    print(iterative_gcd(1997, 615))
    assert recursive_gcd(1997, 615) == recursive_gcd(615, 1997) == iterative_gcd(1997, 615) == iterative_gcd(615, 1997)
