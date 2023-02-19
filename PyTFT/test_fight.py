import pytest

from consts import Tanks, u2tierchamps
from fight import count_victory_points, find_objects_on_arena, find_tiers_on_arena


@pytest.mark.parametrize("objects,points", [(1, 1), (3, 2), (6, 3), (9, 5)])
def test_count_vp(objects, points):
    test_fight = count_victory_points(objects=objects)
    assert test_fight == points


@pytest.mark.parametrize("arena,objects", [(["Skarner'2 - 3", "Mundo'3 - 9", "Jinx'2 - 3"], Tanks)])
def test_find_objects(arena, objects):
    test_find_object = find_objects_on_arena(arena=arena, objects=objects)
    assert test_find_object == 2


@pytest.mark.parametrize("arena,objects", [(["Skarner'2 - 3", "Mundo'3 - 9", "Jinx'2 - 3"], u2tierchamps)])
def test_find_tiers(arena, objects):
    test_find_tier = find_tiers_on_arena(arena=arena, objects=objects)
    assert test_find_tier == 2
