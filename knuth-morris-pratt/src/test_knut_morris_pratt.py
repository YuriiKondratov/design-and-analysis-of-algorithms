import pytest
import main1
import main2


@pytest.mark.parametrize("test_data, result", [
    (("ab", "abab"), ([0, 2])),
    (("abc", "asdlkfj"), ([-1])),
    (("abab", "abababababab"), ([0, 2, 4, 6, 8])),
    (("qwertyui", "qwer"), ([-1])),
    (("qwer", "qwer"), ([0])),
    (("qwert", "qwergqwertqwerhqweryqwerqwerqwqwqwerlkjqeriqweroqern"), ([5]))
])
def test_kmp_1(test_data, result):
    assert main1.knut_morris_pratt(*test_data) == result


@pytest.mark.parametrize("test_data, result", [
    (("defabc", "abcdef"), 3),
    (("asdfg", "adsfg"), -1),
    (("qwert", "qwer"), -1),
    (("abababa", "bababab"), -1),
    (("abababab", "abababab"), 0),
])
def test_kmp_2(test_data, result):
    assert main2.knut_morris_pratt(*test_data) == result
