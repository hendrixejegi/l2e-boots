def check_ingredient_match(recipe, inventory):
    missing_count = 0
    missing_items = []

    for item in recipe:
        if not item in inventory:
            print(item)
            missing_count += 1
            missing_items.append(item)
    
    has_per = ((len(recipe)-missing_count) / len(recipe)) * 100
    return has_per, missing_items
