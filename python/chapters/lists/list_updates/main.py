def smelt_ore(inventory):
    has_iron_ore = inventory[1] == "Iron Ore"
    if has_iron_ore:
        inventory[1] = "Iron Bar"
    return inventory
