# ⚠️ Clear the multiline comments at the top and bottom
# of each line of code to walkthrough the solution as it
# was implemented in the lesson

"""
# Step 1
def unlock_achievement(before_xp, ach_xp, ach_name):

"""

"""
# Step 2
def unlock_achievement(before_xp, ach_xp, ach_name):
  after_xp = before_xp - ach_xp
  print("After xp:", after_xp)
  return None, None
"""

"""
# Step 3
def unlock_achievement(before_xp, ach_xp, ach_name):
  after_xp = before_xp + ach_xp
  alert = f"Achievement: {ach_name}"
  print(alert)
  return after_xp, None
"""

# Step 4
def unlock_achievement(before_xp, ach_xp, ach_name):
  after_xp = before_xp + ach_xp
  alert = f"Achievement Unlocked: {ach_name}"
  print(alert)
  return after_xp, alert
