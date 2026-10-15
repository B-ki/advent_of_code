import pytest
import P2

EXAMPLE= [("L", 68), ("L", 30), ("R", 48), ("L", 5), ("R", 60),
             ("L", 55), ("L", 1), ("L", 99), ("R", 14), ("L", 82)]

@pytest.mark.parametrize("tuple_list, expected", [
    ([("R", 1000)], 10)
    ])
def test_loop_over_input(tuple_list, expected):
    result = P2.loop_over_input(tuple_list)
    assert result == expected


def test_loop_over_input_example():
    assert P2.loop_over_input(EXAMPLE) == 6
