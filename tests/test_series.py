import pytest
from math_series.series import fibonacci, lucas, sum_series

# fibonacci tests

def test_fibonacci_0():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_1():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_2():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_3():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_fibonacci_not_in_sequence():
  actual = fibonacci(-1)
  expected = None
  assert actual == expected

def test_fibonacci_not_an_integer():
  actual = fibonacci('1')
  expected = None
  assert actual == expected

# lucas tests

def test_lucas_0():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_1():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_2():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_3():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lucas_not_in_sequence():
  actual = lucas(-1)
  expected = None
  assert actual == expected

def test_lucas_not_an_integer():
  actual = lucas('1')
  expected = None
  assert actual == expected

# sum_series tests

# fibonacci sum_series
def test_fibonacci_sum_series_0():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_fibonacci_sum_series_1():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_fibonacci_sum_series_2():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_fibonacci_sum_series_3():
  actual = sum_series(3)
  expected = 2
  assert actual == expected

# lucas sum_series
def test_lucas_sum_series_0():
  actual = sum_series(0, 2, 1)
  expected = 2
  assert actual == expected

def test_lucas_sum_series_1():
  actual = sum_series(1, 2, 1)
  expected = 1
  assert actual == expected

def test_lucas_sum_series_2():
  actual = sum_series(2, 2, 1)
  expected = 3
  assert actual == expected

def test_lucas_sum_series_3():
  actual = sum_series(3, 2, 1)
  expected = 4
  assert actual == expected

# edge sum_series
def test_sum_series_not_in_sequence():
  actual = sum_series(-1)
  expected = None
  assert actual == expected

def test_sum_series_not_an_integer():
  actual = sum_series('1')
  expected = None
  assert actual == expected
