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
