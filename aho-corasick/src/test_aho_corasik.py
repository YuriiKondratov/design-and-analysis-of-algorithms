import pytest
from task1 import aho_corasick
from task2 import solve


@pytest.mark.parametrize("test_data, result", [
    (('NTAG', ['TAGT', 'TAG', 'T']), [(2, 2), (2, 3)]),
    (('a', ['b']), []),
    (('abcda', ['abc', 'bc', 'bcda']), [(1, 1), (2, 2), (2, 3)]),
    (('abcabcabcabcabc', ['abc']), [(1, 1), (4, 1), (7, 1), (10, 1), (13, 1)]),
    (('abcdeffedcbadefabc', ['abcdef', 'abc', 'bcd', 'cde', 'def']),
     [(1, 1), (1, 2), (2, 3), (3, 4), (4, 5), (13, 5), (16, 2)]),
])
def test_1(test_data, result):
    assert sorted(aho_corasick(*test_data)) == result


@pytest.mark.parametrize("test_data, result", [
    (('ACTANCA', 'A$$A$', '$'), [1]),
    (('abcdef', 'b', '*'), [2]),
    (('abcdeffbcbfbdbfbbh', '___f___', '_'), [3, 4, 8, 12]),
    (('fbabfabbfcd', 'f___f___', '_'), [1]),
    (('fffabcdeabcdeabcdeff', '__abcd_abc___bcd__', '_'), [2]),
])
def test_2(test_data, result):
    assert solve(*test_data) == result
