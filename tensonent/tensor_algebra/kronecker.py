"""
    kronecker product

    Author: Milad Sadeghi.DM
"""

from numpy import kron


def kronecker(p_1, p_2, *args):
    """
    Kronecker Product for series of tensors, matrices , vectors or scalars

    :param p_1: ndarray, iterable, int, float
    :param p_2: ndarray, iterable, int, float
    :param args: optional or ndarray, iterable, int, float
    :return: ndarray
    """
    res = kron(p_1, p_2)
    if args:
        for item in args:
            res = kron(res, item)
    return res
