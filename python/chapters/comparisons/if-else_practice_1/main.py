def check_high_score(current_player_name, high_scoring_player_name):
  # Bug 1 – The original condition `if True` always evaluates to True,
  # so the function always returns "You are the highest scoring player!"
  # and never reaches the `else` block.
  if current_player_name == high_scoring_player_name:
    return "You are the highest scoring player!"
  else:
    return "You are not the highest scoring player!"