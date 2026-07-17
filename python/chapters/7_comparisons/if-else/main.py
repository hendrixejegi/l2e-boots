def player_status(health):
  # Solution 1: Very good
  if health <= 0:
    return "dead"
  elif health <= 5:
    return "injured"
  else:
    return "healthy"
  
  # Solution 2: Works, but less clean
  # if health > 5:
  #   return "healthy"
  # elif health > 0 and health <= 5:
  #   return "injured"
  # else:
  #   return "dead"

  # Solution 3 (Credit: ChatGPT): Best
  # if health <= 0:
  #       return "dead"
  #   if health <= 5:
  #       return "injured"
  #   return "healthy"

"""
Notes:
  While the first solution would be the expected solution because the topic introduced
  the concept of chaining if statements using "elif" and "else". Solution 2 (commented out)
  makes use of the logical "and" operator to explore the solution from a different angle.
  
  Although both solution 1 and 2 use the same concept of chaining if statements solution 1
  is the better one for the following reasons:

  1. Simpler conditions:
    The first solution takes advantage of the fact the python checks conditions in order.

    elif health <= 5 — At this point you already know health > 0 because the first `if health <= 0` failed.
    so there's no need to write `health > 0 and health <= 5` which makes the second version more verbose.

  2. Less redundant:
    In the second solution, `elif health > 0 and health <= 5`. The `health > 0` check is only there because
    I started from the highest value and worked downward. It repeats information that can often be inferred.

  3. Easier to read:
    The first solution follows a natural progression: Dead --> Injured --> Healthy.

  4. Fewer comparisons:
    The first solution may perform fewer comparisons. For example, if health = 3

    First solution:
      1. health <= 0 -> False
      2. health <= 5 -> True

    Second Solution:
      1. health > 5 -> False
      2. health > 0 -> False
      3. health <= 5 -> True

    The difference is tiny, but the first version is a little more efficient.
"""

"""
Notes:
  The third solution (commented out) is a cleaner version (Credit to GPT). It simplifies it further by not
  relying on the else block. Because each return exits the function, elif and else  aren't necessary here.
"""