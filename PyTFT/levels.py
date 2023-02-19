def get_level(experience_points, level):
    if 12 > experience_points >= 4:
        level = 2
    elif 24 > experience_points >= 12:
        level = 3
    elif 40 > experience_points >= 24:
        level = 4
    elif 60 > experience_points >= 40:
        level = 5
    elif 80 > experience_points >= 60:
        level = 6
    elif 104 > experience_points >= 80:
        level = 7
    elif 132 > experience_points >= 104:
        level = 8
    elif 160 > experience_points >= 132:
        level = 9
    elif experience_points >= 160:
        level = 10
    return level
