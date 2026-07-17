# The prefix 0b is used to indicate that what follows is a binary number in python
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

# The symbol for the bitwise AND operator is &
def get_create_bits(user_permissions):
  return user_permissions & can_create_guild


def get_review_bits(user_permissions):
  return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
  return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
  return user_permissions & can_edit_guild