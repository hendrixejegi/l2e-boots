def factorial(num: int) -> int:
  if num == 0 or num == 1:
    return 1
  
  product = 1

  for n in range(num, 0, -1):
    product *= n

  return product
