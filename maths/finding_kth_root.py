"""
Finding the (real) k-th root of a given degree of a given number
rounding to the nearest given number of decimal places without using ** or pow()
[Problem link]
https://www.geeksforgeeks.org/calculating-n-th-real-root-using-binary-search/
"""


def finding_kth_root(number: float, k: int, decimal_place: int) -> float:
    """
    Implementing binary search to find the k-th root of a number.
    Negative numbers are treated like positive numbers,
    with the minus sign added at the end.

    Parameters
    ----------
    number
      The given number to calculate.

    k
      The degree of the root (e.g. 3rd root, 5th root).

    decimal_place
      The number of decimal places in the final result.

    Returns
    -------
      The k-th root of `number`, rounded to `decimal_place` decimal places.
    
    >>> finding_kth_root(3, 2, 5)
    1.73205
    >>> finding_kth_root(122.683, 10, 7)
    1.6176272
    >>> finding_kth_root(5, 1, 3)
    5.0
    >>> finding_kth_root(0, 2, 2)
    0.0
    >>> finding_kth_root(125.7, 2, 0)
    11.0
    >>> finding_kth_root(-123, 5, 3)
    -2.618
    >>> finding_kth_root(-123, 4, 3)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    >>> finding_kth_root(123, -1, 3)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    if deg < 1:
        raise ValueError("math domain error")

    if deg % 2 == 0 and number < 0:
        raise ValueError("math domain error")

    hi, lo = number, 0.0
    if number < 0:
        hi = -number

    error = 1.0
    for _i in range(decimal_place + 1):
        error /= 10

    while hi - lo >= error:  # Precision is not reached, continue looping
        mid = (hi + lo) / 2
        product = 1.0
        for _i in range(deg):
            product *= mid

        if product > abs(number):  # Overestimation, higher bound decreases to mid
            hi = mid

        else:  # Underestimation, lower bound increases to mid
            lo = mid

    if number < 0:
        return -round(lo, decimal_place)

    return round(lo, decimal_place)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
