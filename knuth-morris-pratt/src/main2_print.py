def prefix(s: str) -> list[int]:
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        pi[i] = k
        #print(str(i) + ": " + str(pi[i]))
    return pi


def knut_morris_pratt(pattern: str, text: str) -> int:
    p_len, t_len = len(pattern), len(text)

    if p_len != t_len / 2:
        return -1

    print("Префикс-функция для подстроки: ")
    pi = prefix(pattern)
    print(str(pi) + "\n")

    q = 0
    for i in range(t_len):
        print("Номер итерации: " + str(i))
        print("Длина совпадающего отрезка: " + str(q) + "\n")
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == p_len:
            return i - p_len + 1
    return -1


if __name__ == "__main__":
    pattern, text = input(), input()
    print("Ищем подстроку: " + text)
    print("В строке: " + pattern * 2 + "\n")
    print(knut_morris_pratt(text, pattern * 2))
