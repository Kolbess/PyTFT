import pytest
from PyTFT import upgrade, fight


@pytest.mark.parametrize("b,bench", [(["Skarner'1 - 1", "Skarner'1 - 1", "Skarner'1 - 1"], ["Skarner'2 - 3", "–", "–"]),
                                     (["Skarner'2 - 3", "Skarner'2 - 3", "Skarner'2 - 3"], ["Skarner'3 - 9", "–", "–"]),
                                     (["Yorick'2 - 12", "Yorick'2 - 12", "Yorick'2 - 12"], ["Yorick'3 - 36", "–", "–"])]
                         )
def test_upgrade(b, bench):
    test_upg = upgrade(b=b)
    assert test_upg == bench


@pytest.mark.parametrize("health, win, loss, money, arena, enemyarena", [(100, 1, 0, 13,
                                                                         ["Skarner'2 - 3", "Mundo'2 - 3"],
                                                                         ["Skarner'1 - 1", "Skarner'1 - 1"])])
def test_fight(health, win, loss, money, arena, enemyarena):
    test1, test2, test3, test4 = fight(health=100, win=0, loss=0, money=5, a=arena, ea=enemyarena)
    assert test1 == health
    assert test2 == win
    assert test3 == loss
    assert test4 == money
