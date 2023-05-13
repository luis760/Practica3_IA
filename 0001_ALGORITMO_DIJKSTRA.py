import sys

def dijkstra(graph, start, end):
    unvisited = {node: sys.maxsize for node in graph}
    unvisited[start] = 0
    visited = {}
    predecessors = {}

    while unvisited:
        current_node = min(unvisited, key=unvisited.get)
        visited[current_node] = unvisited[current_node]
        del unvisited[current_node]

        for neighbor, distance in graph[current_node].items():
            if neighbor in visited:
                continue
            new_distance = visited[current_node] + distance
            if new_distance < unvisited[neighbor]:
                unvisited[neighbor] = new_distance
                predecessors[neighbor] = current_node

    path = []
    current_node = end
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        except KeyError:
            print("No se puede llegar al destino desde el nodo de inicio")
            break
    path.insert(0, start)
    return visited[end], path

if __name__ == '__main__':
    graph = {
        'A': {'B': 2, 'C': 1},
        'B': {'A': 2, 'D': 4, 'E': 2},
        'C': {'A': 1, 'F': 3},
        'D': {'B': 4, 'E': 3},
        'E': {'B': 2, 'D': 3, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }

    distance, path = dijkstra(graph, 'A', 'F')
    print(f"La distancia más corta desde A hasta F es: {distance}")
    print(f"El camino más corto desde A hasta F es: {' -> '.join(path)}")