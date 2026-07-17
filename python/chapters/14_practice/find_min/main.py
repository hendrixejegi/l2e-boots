def find_min(nums: list[int]) -> int | float:
  min_num = float("inf")

  if len(nums) == 0:
    return min_num
  
  for n in nums:
    if n < min_num:
      min_num = n

  return min_num
