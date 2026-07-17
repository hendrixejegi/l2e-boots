"""
Question:
  In the code sample, what will happen?

Answer:
  The program will crash with an uncaught exception

Explanation:
  `raise Exception("zero division")` raises a general `Exception`, but the except only catches `ZeroDivisionError`.
"""