def find_objects_on_arena(arena, objects):
    objects_counter = 0
    for i in arena:
        for j in objects:
            if i[:-6] == j[:-4]:
                objects_counter += 1
    return objects_counter


def find_tiers_on_arena(arena, objects):
    objects_counter = 0
    for i in arena:
        for j in objects:
            if i == j:
                objects_counter += 1
    return objects_counter


def count_victory_points(objects):
    points = 0
    if objects == 9:
        points += 5
    elif objects >= 6:
        points += 3
    elif objects >= 3:
        points += 2
    elif objects >= 1:
        points += 1
    return points
