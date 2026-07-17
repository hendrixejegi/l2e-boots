def divide_list(nums: list[int], divisor: int) -> list[float]:
  result: list[float] = []

  for n in nums:
    result.append(n / divisor)

  return result
