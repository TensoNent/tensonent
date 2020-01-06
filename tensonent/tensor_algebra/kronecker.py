"""
    kronecker product

    Author: Milad Sadeghi.DM
"""

from typing import Union, Iterable
from numpy import kron, ndarray


def kronecker(p_1: Union[ndarray, Iterable, float, int],
              p_2: Union[ndarray, Iterable, float, int],
              *args: Union[ndarray, Iterable, float, int]) -> ndarray:
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
