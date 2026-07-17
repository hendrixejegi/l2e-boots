def take_magic_damage(health, resist, amp, spell_power):
  max_damage = amp * spell_power
  actual_damage_dealt = max_damage - resist
  new_health = health - actual_damage_dealt
  return new_health
