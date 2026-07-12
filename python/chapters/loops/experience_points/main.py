def calculate_experience_points(level):
  # Players start at level 1 with 0 XP.
  total_xp = 0

  # No previous levels exist before level 2, so return early.
  if level < 2:
    return total_xp

  # Sum the XP required for each completed level.
  # The current level is excluded because the player is
  # still earning XP toward the next level.
  # For example, a level 3 player has completed levels 1 and 2,
  # so only those XP values are included.
  for i in range(1, level):
    total_xp += 5 * i

  return total_xp

