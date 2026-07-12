def countdown_to_start():
  for count in range(10, 0, -1):
    if count == 1:
      print(f"{count}...Fight!")
    else:
      print(f"{count}...")


# Don't edit below this line


def test():
  print("Counting down to match start:")
  countdown_to_start()
  print("=====================================")


def main():
  test()


main()