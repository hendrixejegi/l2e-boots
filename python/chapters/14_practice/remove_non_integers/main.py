def remove_nonints(nums: list[object]) -> list[int]:
    new_list: list[int] = []

    for item in nums:
        if type(item) == int:
            new_list.append(item)

    return new_list
