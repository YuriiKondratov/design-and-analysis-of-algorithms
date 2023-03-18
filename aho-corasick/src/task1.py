class Node:
    def __init__(self, suf_link=None):
        self.sub_nodes = {}
        self.suf_link = suf_link
        self.patterns = []


class Trie:
    def __init__(self, patterns: list[str]):
        self.__create_tree(patterns)
        self.__add_links()

    def __create_tree(self, patterns):
        self.root = Node()
        for ind, pattern in enumerate(patterns):
            node = self.root
            for symbol in pattern:
                node = node.sub_nodes.setdefault(symbol, Node(self.root))
            node.patterns.append(ind)

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
                node.patterns += node.suf_link.patterns


def aho_corasick(string, patterns):
    trie = Trie(patterns)
    ans = []
    node = trie.root
    for i in range(len(string)):
        while node is not None and string[i] not in node.sub_nodes:
            node = node.suf_link
        if node is None:
            node = trie.root
            continue
        node = node.sub_nodes[string[i]]
        for pattern in node.patterns:
            ans.append((i - len(patterns[pattern]) + 2, pattern + 1))
    return ans


if __name__ == "__main__":
    text = input()
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())

    result = sorted(aho_corasick(text, patterns))
    for i in result:
        print(i[0], i[1])

