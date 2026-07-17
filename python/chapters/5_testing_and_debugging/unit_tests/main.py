def total_xp(level, xp_to_add):
  xp_per_level = 100

  xp_gained_from_level = level * xp_per_level

  total = xp_gained_from_level + xp_to_add
  return total

