import csv


def get_points_for_tiers():
    d = {}
    with open('points_for_tiers.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            d[row[0]] = row[1:]
    return d


data = get_points_for_tiers()
