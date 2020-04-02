def find_eulerian_tour(graph):
    stack = [];
    tour = []

    stack.append(graph[0][0])

    while len(stack) > 0:
        v = stack[len(stack) - 1]

        degree = get_degree(v, graph)

        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, graph)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
    return tour


def get_degree(v, graph):
    degree = 0
    for (x, y) in graph:
        if v == x or v == y:
            degree += 1

    return degree


def get_edge_and_index(v, graph):
    edge = ();
    index = -1

    for i in range(len(graph)):
        if (v == graph[i][0] or v == graph[i][1]):
            edge, index = graph[i], i
            break

    return index, edge


graph = [(0, 1), (1, 5), (1, 7), (4, 5),
         (4, 8), (1, 6), (3, 7), (5, 9),
         (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

print((find_eulerian_tour(graph)))
