import pytest
from PyTFT import upgrade


@pytest.mark.parametrize("b,bench", [(["Skarner'1 - 1", "Skarner'1 - 1", "Skarner'1 - 1"], ["Skarner'2 - 3", "–", "–"]),
                                     (["Skarner'2 - 3", "Skarner'2 - 3", "Skarner'2 - 3"], ["Skarner'3 - 9", "–", "–"])]
                         )
def test_upgrade(b, bench):
    test_upg = upgrade(b=b)
    assert test_upg == bench
