def main():
  # damage: 8 million, time: 45
  calculate_dps(8e6, 45)
  # damage: 10 million, time: 49
  calculate_dps(1e7, 49)


# Don't edit below this line


def calculate_dps(damage, time):
  dps = damage / time
  print(f"Damage per second: {dps}")
  print("=====================================")


main()
