def prefix(s: str) -> list[int]:
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        pi[i] = k
    return pi


def knut_morris_pratt(pattern, text):
    pi = prefix(pattern + '#' + text)
    res = []
    for i, l in enumerate(pi):
        if l == len(pattern):
            res.append(i - len(pattern) * 2)
    return res if res else [-1]


if __name__ == "__main__":
    pattern, text = input(), input()
    print(*knut_morris_pratt(pattern, text), sep=',')
