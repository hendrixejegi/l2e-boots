def does_attack_hit(attack_roll, armor_class):
  should_hit = (not attack_roll == 1 and attack_roll >= armor_class) or attack_roll == 20
  if should_hit:
    return True
  return False