def number_sum(n: int) -> int:
  sum = 0

  if n < 1:
    return sum
  
  for i in range(1, n+1):
    sum += i
  
  return sum
