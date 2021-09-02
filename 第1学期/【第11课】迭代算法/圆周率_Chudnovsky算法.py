from decimal import Decimal, getcontext
from math import ceil, factorial


def pi(precision=14):
    """
    Chudnovsky算法是一种快速计算π位数的方法, 基于Ramanujan的π公式。
    PI = constant_term / ((multinomial_term * linear_term) / exponential_term)
        where constant_term = 426880 * sqrt(10005)
    The linear_term and the exponential_term can be defined iteratively as follows:
        L_k+1 = L_k + 545140134            where L_0 = 13591409
        X_k+1 = X_k * -262537412640768000  where X_0 = 1
    The multinomial_term is defined as follows:
        6k! / ((3k)! * (k!) ^ 3)
            where k is the k_th iteration.
    This algorithm correctly calculates around 14 digits of PI per iteration
    """
    if not isinstance(precision, int):
        raise TypeError("Undefined for non-integers")
    elif precision < 1:
        raise ValueError("Undefined for non-natural numbers")
    getcontext().prec = precision
    num_iterations = ceil(precision / 14)
    constant_term = 426880 * Decimal(10005).sqrt()
    exponential_term = 1
    linear_term = 13591409
    partial_sum = Decimal(linear_term)
    for k in range(1, num_iterations):
        multinomial_term = factorial(6 * k) // (factorial(3 * k) * factorial(k) ** 3)
        linear_term += 545140134
        exponential_term *= -262537412640768000
        partial_sum += Decimal(multinomial_term * linear_term) / exponential_term
    return str(constant_term / partial_sum)[:-1]


while True:
    n = int(input("输入需要计算的位数："))
    print("π的前{}位是：{}".format(n, pi(n)))
