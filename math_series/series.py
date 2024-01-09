def fibonacci(n):

  if type(n) != int:
    return None

  if n < 0:
    return None

  if n == 0:
    return 0
  
  if n == 1:
    return 1
  
  return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

  if type(n) != int:
    return None

  if n < 0:
    return None
  
  if n == 0:
    return 2
  
  if n == 1:
    return 1
  
  return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n_0 = 0, n_1 = 1):

  if type(n) != int:
    return None

  if n < 0:
    return None
  
  if n == 0:
    return n_0
  
  if n == 1:
    return n_1
  
  return sum_series(n - 1, n_0, n_1) + sum_series(n - 2, n_0, n_1)
