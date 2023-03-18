class Node:
    def __init__(self, suf_link=None, name="root"):
        self.sub_nodes = {}
        self.suf_link = suf_link
        self.patterns = []
        self.name = name


class Trie:
    def __init__(self, patterns: list[str]):
        self.nodes = []

        print("Построение бора: ")
        self.__create_tree(patterns)
        print()

        print("Построение автомата: ")
        self.__add_links()
        print()

        print("Построенный автомат: ")
        for x in self.nodes:
            print('''  * Вершина: {}
    Суффиксная ссылка на: {}
    Слова, оканчивающиеся в вершине: {}
    Вершины-потомки: {}'''.format(
                x.name, x.suf_link.name if x.suf_link is not None else None,
                ", ".join([patterns[y] for y in x.patterns]), ", ".join(str(z) for z in x.sub_nodes)))
        print()

    def __create_tree(self, patterns):
        self.root = Node()
        self.nodes.append(self.root)
        for ind, pattern in enumerate(patterns):
            node = self.root
            for symbol in pattern:
                print('\tДобавлена вершна ' + symbol + ' с родителем ' + node.name + '')
                node = node.sub_nodes.setdefault(symbol, Node(self.root, symbol))
                self.nodes.append(node)
            node.patterns.append(ind)
            print("  * Закончено добавление слова: " + patterns[ind])

    def __add_links(self):
        queue = [x for x in self.root.sub_nodes.values()]

        while queue:
            cur = queue.pop(0)

            for symbol, node in cur.sub_nodes.items():
                queue.append(node)

                link = cur.suf_link
                while not (link is None or symbol in link.sub_nodes):
                    link = link.suf_link

                node.suf_link = link.sub_nodes[symbol] if link else self.root
                print("\tДобавлена суффиксная ссылка: " + node.name + " -> " + node.suf_link.name)
                node.patterns += node.suf_link.patterns


def aho_corasick(string, patterns):
    trie = Trie(patterns)
    ans = []
    node = trie.root
    print("Работа алгоритма на строке {}:".format(string))
    for i in range(len(string)):
        print("\tНомер символа в строке: " + str(i))
        while node is not None and string[i] not in node.sub_nodes:
            if node.suf_link is not None:
                print("\t\tПереход по суффиксной ссылке: {} -> {}".format(node.name, node.suf_link.name))
            node = node.suf_link
        if node is None:
            node = trie.root
            continue
        node = node.sub_nodes[string[i]]
        for p_i in node.patterns:
            print("\t\tНайден паттерн: " + patterns[p_i] + " ")
            ans.append((i - len(patterns[p_i]) + 1, p_i))

    print()
    return ans


def generate_patterns(pattern, wild_card):
    parts = list(filter(bool, pattern.split(wild_card)))
    start_indices = []
    flag = 1
    for i, c in enumerate(pattern):
        if c == wild_card:
            flag = 1
            continue
        if flag:
            start_indices.append(i)
            flag = 0
    return parts, start_indices


if __name__ == "__main__":
    text = input()
    p = input()
    wc = input()
    patterns, starts = generate_patterns(p, wc)

    print("Сгенерированные паттерны: ")
    print(*patterns, sep=", ")
    print()

    indices = aho_corasick(text, patterns)
    c = [0] * len(text)
    for i, p_i in indices:
        index = i - starts[p_i]
        if 0 <= index < len(c):
            c[index] += 1

    print("Список с количествами совпавших паттернов: ")
    print("\t", c, "\n")

    res = []
    for i in range(len(c) - len(p) + 1):
        if c[i] == len(patterns):
            res.append(i + 1)
    print("Результат: ")
    print(*res, sep="\n")
