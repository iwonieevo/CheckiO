def dijkstra(graph: list[list[str, str, int]], source: str) -> list[(str, str, int)]:
    """
    Dijkstra's algorithm for finding the shortest paths between nodes in a weighted graph. More info here: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    :param graph: All connections in the graph stored in a list of lists, e.g. [v_1, v_2, x] means there is a direct connection between v_1 and v_2 with Euclidean distance equal to x
    :param source: Source vertex, start of the whole graph
    :return: Returns a dictionary with nodes as keys and a tuple of the shortest path, and it's distance; {node: (path, distance_from_source)}
    """
    dist: {str: int} = {}  # storing current distance from source to vertex, if there is no connection, distance == 0
    prev: {str: str} = {}  # storing path from source to vertex, if there is no connection, path == ""
    for v1, v2, _ in graph:  # filling distances and paths with default values
        dist[v1] = float('inf')
        dist[v2] = float('inf')
        prev[v1]: str = ""
        prev[v2]: str = ""
    dist[source] = 0  # the source vertex is considered to have no connection to itself
    queue: list[str] = list(dist.keys())  # adding each vertex to queue

    while queue:
        u: str = max(dist, key=dist.get)
        for vertex in queue:
            if dist[vertex] <= dist[u]:
                u = vertex
        queue.remove(u)  # removing the node with the smallest distance from the queue and saving it in u

        for all_v in graph:
            if u not in all_v[:-1]:  # checking for neighbours of node u
                continue
            v = all_v[:-1][all_v[:-1].index(u) - 1]
            if v not in queue:  # checking if neighbour is in the queue
                continue
            alt = dist[u] + all_v[-1]
            if alt < dist[v]:  # if the distance through neighbour node is shorter, it is the new distance for that node
                dist[v] = alt
                prev[v] = prev.get(u, "") + u
    for key in dist:  # replacing distances of all nodes that have no connection to the source node with 0
        if dist[key] == float('inf'):
            dist[key] = 0

    return dict(sorted(zip(dist.keys(), zip(prev.values(), dist.values()))))  # returning respectfully: path, node, distance from source


def cheapest_flight(costs: list, a: str, b: str) -> int:
    return dijkstra(costs, a)[b][1]


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
