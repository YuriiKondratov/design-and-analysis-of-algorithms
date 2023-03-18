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


if __name__ == "__main__":
    text = input()
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())

    result = sorted(aho_corasick(text, patterns))

    for i, p_i in result:
        p_len = len(patterns[p_i])
        text = text[:i] + "_" * p_len + text[i + p_len:]

    print("Строка с вырезанными паттернами: \n\t", end='')
    print("".join(text.split("_")))
