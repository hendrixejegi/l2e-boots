# The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
# The max players on a "medium" server: 10,240,000,000,000,000,000
# The max players on a "large" server: 102,400,000,000,000,000,000

def max_players_on_server():
  # There are two solutions to this exercise

  # 1. Using underscores
  # max_players_small_server = 1_024_000_000_000_000_000
  # max_players_medium_server = 10_240_000_000_000_000_000
  # max_players_large_server = 102_400_000_000_000_000_000

  # 2. Using scientific notation (e or E)
  max_players_small_server = 1.024e18
  max_players_medium_server = 1.024e19
  max_players_large_server = 1.024e20

  return max_players_small_server, max_players_medium_server, max_players_large_server
