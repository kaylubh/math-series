def fibonacci(n):
  """
  Generates a number at a requested index(`n`) from the Fibonacci sequence. `n` begins at the 0 index.

  Parameters:
  `n` (integer): The index of the Fibonacci sequence numbers to return

  Returns: 
  integer: The number from the Fibonacci sequence at the requested index
  """

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
  """
  Generates a number at a requested index(`n`) from the Lucas sequence. `n` begins at the 0 index.

  Parameters:
  `n` (integer): The index of the Lucas sequence numbers to return

  Returns: 
  integer: The number from the Lucas sequence at the requested index
  """

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
  """
  Generates a number at a requested index(`n`) from a sequence which sums the preceding two numbers in the series. Defaults to the Fibonacci sequence if the two starting numbers of the sequence are not provided. `n` begins at the 0 index.
  `n` = (`n` - 1) + (`n` - 2)

  Parameters:
  `n` (integer): The index of the sequence numbers to return
  `n_0` (integer)(default = 0): The first number in the sequence
  `n_1` (integer)(default = 1): The second number in the sequence

  Returns: 
  integer: The number from the sequence at the requested index
  """

  if type(n) != int:
    return None

  if n < 0:
    return None
  
  if n == 0:
    return n_0
  
  if n == 1:
    return n_1
  
  return sum_series(n - 1, n_0, n_1) + sum_series(n - 2, n_0, n_1)
