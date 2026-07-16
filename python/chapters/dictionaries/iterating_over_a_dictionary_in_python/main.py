def get_most_common_enemy(enemies_dict):
  max_so_far = float("-inf")
  enemy_name = None

  for enemy in enemies_dict:
    if enemies_dict[enemy] > max_so_far:
      max_so_far = enemies_dict[enemy]
      enemy_name = enemy
      
  return enemy_name

