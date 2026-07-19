def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_chars(text: str) -> dict[str, int]:
    count: dict[str, int] = {}

    for char in text:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1

    return count

def sort_on(count: tuple[str, int]) -> int:
    return count[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    unsorted_list: list[tuple[str, int]] = []

    for char in counts:
        unsorted_list.append((char, counts[char]))

    sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)

    return sorted_list
