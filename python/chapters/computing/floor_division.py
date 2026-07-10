"""
Question:
  What would be the result of 11 // 2 ?

Answer:
  5

Explanation:
  The result of dividing 11 by 2 is 5.5

  The essence of the floored division is to round down to the nearest integer

  so the result is 5 ✅

Notes:
  The reason rounding down a negative float like -2.333 (from the lesson example)
  results in -3 is because Python's "rounding down" means rounding towards negative
  infinity, not "chopping off the decimal part."

  Example:
    2.333 = 2
    -2.333 = -3
  
  Think of the number line:
    <---- -4 ---- -3 ---- -2 ---- -1 ---- 0 ---- 1 ---->
                        ↑
                        -2.333
    The greatest integer <= -2.333 is -3

  Mathematically the floor function is defined as:
    floor(x) = the greatest integer <= x

    2 <= 2.333
    -3 <= -2.333
"""