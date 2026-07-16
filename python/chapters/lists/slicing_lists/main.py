def get_champion_slices(champions):
    slice_1 = champions[2:]
    slice_2 = champions[:-1]
    slice_3 = champions[::2]
    return slice_1, slice_2, slice_3
