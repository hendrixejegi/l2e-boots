# ⚠️ Clear the multiline comments at the top and bottom
# of each line of code to walkthrough the solution as it
# was implemented in the lesson

"""
# Raw code
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
  msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
  return msg
"""

"""
# Fix one
def create_stats_message(strength, wisdom, dexterity):
  total = strength + wisdom + dexterity
  msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
  return msg
"""


# Fix two
def create_stats_message(strength, wisdom, dexterity):
  total = strength + wisdom + dexterity
  msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
  return msg

