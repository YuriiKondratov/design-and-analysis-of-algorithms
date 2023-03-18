import pytest
from ford_fulkerson import ford_fulkerson

"""
1) Тест из задания
2) Тест на рёбра с нулевым потоком
3) Тест на двойные ребра
4) Тест на применение остаточных ребер
5) Тест с тяжёлыми ребрами но маленьким потоком
"""


@pytest.mark.parametrize("test_data, result", [
    (
            ({'a': {'b': 7, 'c': 6}, 'b': {'d': 6}, 'c': {'f': 9}, 'd': {'e': 3, 'f': 4}, 'f': {}, 'e': {'c': 2}}, 'a', 'f'),
            (12, {'a': {'b': 1, 'c': 0}, 'b': {'d': 0, 'a': 6}, 'c': {'f': 1, 'a': 6, 'e': 2}, 'd': {'e': 1, 'f': 0, 'b': 6}, 'f': {'d': 4, 'c': 8}, 'e': {'c': 0, 'd': 2}})
    ),
    (
            ({'a': {'b': 7, 'c': 6}, 'b': {'d': 6}, 'c': {'f': 6}, 'd': {'e': 3, 'f': 4}, 'f': {}, 'e': {'c': 2}}, 'a', 'f'),
            (10, {'a': {'b': 3, 'c': 0}, 'b': {'d': 2, 'a': 4}, 'c': {'f': 0, 'a': 6}, 'd': {'e': 3, 'f': 0, 'b': 4}, 'f': {'d': 4, 'c': 6}, 'e': {'c': 2}})
    ),
    (
            ({'a': {'b': 5, 'c': 9}, 'b': {'a': 7}, 'c': {}}, 'b', 'c'),
            (7, {'a': {'b': 12, 'c': 2}, 'b': {'a': 0}, 'c': {'a': 7}})
    ),
    (
            ({'a': {'b': 4, 'e': 7}, 'b': {'f': 4, 'c': 5}, 'e': {'c': 3}, 'f': {'d': 9}, 'c': {'d': 4}, 'd': {}}, 'a', 'd'),
            (7, {'a': {'b': 0, 'e': 4}, 'b': {'f': 1, 'c': 4, 'a': 4}, 'e': {'c': 0, 'a': 3}, 'f': {'d': 6, 'b': 3}, 'c': {'d': 0, 'b': 1, 'e': 3}, 'd': {'c': 4, 'f': 3}})
    ),
    (
            ({'a': {'b': 1000, 'c': 1000}, 'b': {'d': 1, 'e': 1}, 'c': {'d': 1, 'e': 1}, 'd': {'f': 1}, 'e': {'f': 1}, 'f': {}}, 'a', 'f'),
            (2, {'a': {'b': 1000, 'c': 998}, 'b': {'d': 1, 'e': 1}, 'c': {'d': 0, 'e': 0, 'a': 2}, 'd': {'f': 0, 'c': 1}, 'e': {'f': 0, 'c': 1}, 'f': {'e': 1, 'd': 1}})
    )
])
def test_ford_fulkerson(test_data, result):
    assert ford_fulkerson(*test_data) == result