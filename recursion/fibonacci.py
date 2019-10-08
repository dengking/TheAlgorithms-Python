# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 17:23
# @File    : fibonacci
import unittest


def recursive_fibonacci(n):
    """
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2)
    :param n:
    :return:
    """
    if n < 0:
        raise Exception('n should be bigger than or equal to 0')
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci(n):
    """
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2)
    :param n:
    :return:
    """
    if n < 0:
        raise Exception('n should be bigger than or equal to 0')
    f_0 = f_1 = 1
    if n == 0 or n == 1:
        return 1
    i = 2
    while i <= n:
        f_i = f_0 + f_1
        f_1, f_0, i = f_i, f_1, i+1
    return f_i


class MyTestCase(unittest.TestCase):
    """

    """

    def test_recursive_fibonacci_invalid_argument(self):
        with self.assertRaises(Exception) as context:
            recursive_fibonacci(-1)
        self.assertTrue('n should be bigger than or equal to 0' in str(context.exception))

    def test_iterative_fibonacci_invalid_argument(self):
        with self.assertRaises(Exception) as context:
            iterative_fibonacci(-1)
        self.assertTrue('n should be bigger than or equal to 0' in str(context.exception))


if __name__ == "__main__":
    assert recursive_fibonacci(0) == iterative_fibonacci(0) == 1
    assert recursive_fibonacci(1) == iterative_fibonacci(1) == 1
    assert recursive_fibonacci(2) == iterative_fibonacci(2) == 2
    assert recursive_fibonacci(3) == iterative_fibonacci(3) == 3
    assert recursive_fibonacci(4) == iterative_fibonacci(4) == 5
    unittest.main()
