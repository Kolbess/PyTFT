import pytest
from levels import get_level


@pytest.mark.parametrize("experience_points,level", [(145, 9), (6, 2), (70, 6), (92, 7), (45, 5), (30, 4), (16, 3),
                                                     (124, 8), (180, 10)])
def test_levels(experience_points, level):
    test_level = get_level(experience_points=experience_points, level=1)
    assert test_level == level
