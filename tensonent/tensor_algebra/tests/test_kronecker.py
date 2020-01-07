"""
    Testing kronecker product

    Author: Milad Sadeghi.DM
"""

from numpy import array
from tensonent.tensor_algebra import kronecker

M_1 = array([[1, 2, 3],
             [4, 5, 6]])  # 2d array

M_2 = array([[1, 2],
             [3, 4]])  # 2d array

M_3 = array([[5, 6],
             [7, 8],
             [9, 10]])  # 2d array

# 2d array
EXPECTED = array([[5, 6, 10, 12, 10, 12, 20, 24, 15, 18, 30, 36],
                  [7, 8, 14, 16, 14, 16, 28, 32, 21, 24, 42, 48],
                  [9, 10, 18, 20, 18, 20, 36, 40, 27, 30, 54, 60],
                  [15, 18, 20, 24, 30, 36, 40, 48, 45, 54, 60, 72],
                  [21, 24, 28, 32, 42, 48, 56, 64, 63, 72, 84, 96],
                  [27, 30, 36, 40, 54, 60, 72, 80, 81, 90, 108, 120],
                  [20, 24, 40, 48, 25, 30, 50, 60, 45, 54, 60, 72],
                  [28, 32, 56, 64, 35, 40, 70, 80, 63, 72, 84, 96],
                  [36, 40, 72, 80, 45, 50, 90, 100, 81, 90, 108, 120],
                  [60, 72, 80, 96, 75, 90, 100, 120, 90, 108, 120, 144],
                  [84, 96, 112, 128, 105, 120, 140, 160, 126, 144, 168, 192],
                  [108, 120, 144, 160, 135, 150, 180, 200, 162, 180, 216, 240]])


def test_kronecker_for_3_array():
    """
    kronecker product for a series of 2d arrays containing 3 array
    :return: ndarray
    """

    result = kronecker(M_1, M_2, M_3)

    assert result.all() == EXPECTED.all()
