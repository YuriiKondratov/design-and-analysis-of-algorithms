import heapq


def heuristic(a: str, b: str) -> int:
    return abs(ord(b) - ord(a))


def sort_vertices(graph: dict[str: tuple[str, float]], goal):
    for vert in graph:
        graph[vert].sort(key=lambda x: heuristic(x[0], goal))


def find_path(goal: str, paths: dict[str: str]) -> str:
    path = goal
    prev = paths[goal]
    while prev is not None:
        path = prev + path
        prev = paths[prev]
    return path


def a_star(initial: str, goal: str, graph: dict[str: list[tuple[str, float]]]):
    path_cost = {initial: 0}
    paths = {initial: None}
    queue = []
    heapq.heappush(queue, (0, initial))

    while len(queue):
        current = heapq.heappop(queue)[1]

        if current == goal:
            break

        for node in graph[current]:
            cost = path_cost[current] + node[1]
            if node[0] not in path_cost or cost < path_cost[node[0]]:
                path_cost[node[0]] = cost
                priority = cost + heuristic(goal, node[0])
                heapq.heappush(queue, (priority, node[0]))
                paths[node[0]] = current

    return paths


def read() -> tuple[str, str, dict]:
    graph = {}
    initial_v, goal_v = input().split()

    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        start, end, weight = line.split()
        weight = float(weight)
        if start in graph:
            graph[start].append((end, weight))
        else:
            graph[start] = [(end, weight)]
        if end not in graph:
            graph[end] = []

    return initial_v, goal_v, graph


def solve(initial: str, goal: str, graph: dict[str: list[tuple[str, float]]]):
    sort_vertices(graph, goal)
    paths = a_star(initial, goal, graph)
    return find_path(goal, paths)


if __name__ == '__main__':
    initial, goal, graph = read()
    print(solve(initial, goal, graph))
