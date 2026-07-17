def meditate(mana, max_mana, num_potions):
  while mana < max_mana and not num_potions == 0:
      mana += 1
      num_potions -= 1
  return mana, num_potions
