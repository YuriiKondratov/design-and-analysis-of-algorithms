from heapq import *
from copy import deepcopy


def read():
    graph = {}
    n = int(input())
    start = input()
    end = input()
    for i in range(n):
        s, e, w = input().split()
        w = int(w)
        if s in graph:
            graph[s][e] = w
        else:
            graph[s] = {e: w}
        if e not in graph:
            graph[e] = {}
    return graph, start, end


def find_path(graph, start, end):
    graph = deepcopy(graph)
    p_queue = []

    for adj in graph[start]:
        dist = abs(ord(start) - ord(adj))
        heappush(p_queue, (dist, adj, start, graph[start][adj]))
    graph[start] = {}

    while p_queue:
        edge = heappop(p_queue)
        if edge[3] <= 0:
            continue
        if edge[1] == end:
            return edge[2] + edge[1], edge[3]
        for adj in graph[edge[1]]:
            dist = abs(ord(adj) - ord(edge[1]))
            path = edge[2] + edge[1]
            min_weight = min(edge[3], graph[edge[1]][adj])
            heappush(p_queue, (dist, adj, path, min_weight))
        graph[edge[1]] = {}

    return "", 0


def ford_fulkerson(graph, start, end):
    graph = deepcopy(graph)
    path, flow = find_path(graph, start, end)
    max_flow = flow
    while path:
        for s, e in zip(path[:-1], path[1:]):
            graph[s][e] -= flow
            if s in graph[e]:
                graph[e][s] += flow
            else:
                graph[e][s] = flow
        path, flow = find_path(graph, start, end)
        max_flow += flow
    return max_flow, graph


def main():
    graph, start, end = read()
    flow, residual_graph = ford_fulkerson(graph, start, end)

    graph = dict(sorted(graph.items()))
    for v in graph:
        graph[v] = dict(sorted(graph[v].items()))

    print(flow)
    for s in graph:
        for e in graph[s]:
            cur_flow = graph[s][e] - residual_graph[s][e]
            print(s, e, cur_flow if cur_flow > 0 else 0)


if __name__ == "__main__":
    main()
