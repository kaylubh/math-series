import pytest
from math_series.series import fibonacci

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

def test_fibonacci_3():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_fibonacci_4():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_fibonacci_5():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected

def test_fibonacci_6():
  actual = fibonacci(6)
  expected = 8
  assert actual == expected

def test_fibonacci_7():
  actual = fibonacci(7)
  expected = 13
  assert actual == expected

def test_fibonacci_not_in_sequence():
  actual = fibonacci(-1)
  expected = None
  assert actual == expected

def test_fibonacci_not_an_integer():
  actual = fibonacci('1')
  expected = None
  assert actual == expected