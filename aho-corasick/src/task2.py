# put your python code here


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
            ans.append((i - len(patterns[pattern]) + 1, pattern))
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


def solve(text, pattern, wild_card):
    patterns, starts = generate_patterns(pattern, wild_card)
    indices = aho_corasick(text, patterns)
    c = [0] * len(text)
    for i, p_i in indices:
        index = i - starts[p_i]
        if 0 <= index < len(c):
            c[index] += 1

    res = []
    for i in range(len(c) - len(pattern) + 1):
        if c[i] == len(patterns):
            res.append(i + 1)
    return res


if __name__ == "__main__":
    txt = input()
    p = input()
    wc = input()
    ans = solve(txt, p, wc)
    print(*ans, sep="\n")
