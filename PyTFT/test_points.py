
from points import get_points_for_tiers, data


def test_get_points_for_tiers():
    test_points = get_points_for_tiers()
    assert test_points == data
