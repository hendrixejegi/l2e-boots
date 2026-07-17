def count_vowels(text):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

  total_vowels = 0
  unique_vowels = set()

  for c in text:
    if c in vowels:
      total_vowels += 1
      unique_vowels.add(c)
  
  return total_vowels, unique_vowels
