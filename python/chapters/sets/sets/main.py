# Method 1 - Iteration
def remove_duplicates(spells):
  found_spells = set()
  unique_spells = []

  for spell in spells:
    is_found = (spell in found_spells)
    if not is_found:
      unique_spells.append(spell)
      found_spells.add(spell)
  
  return unique_spells

# Method 2 - Set Conversion
def remove_duplicates(spells):
  unique_set = set(spells)
  unique_list = list(unique_set)
  return unique_list
