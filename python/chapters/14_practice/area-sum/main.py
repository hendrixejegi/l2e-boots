def area_sum(rectangles: list[dict[str, int]]) -> int:
  sum = 0

  for rect in rectangles:
    area = rect["height"] * rect["width"]
    sum += area
  
  return sum
