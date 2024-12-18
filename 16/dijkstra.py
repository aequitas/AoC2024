from queue import PriorityQueue
from collections import defaultdict

def dijkstra_all_paths(graph, start):
    # Priority queue for maintaining the minimum distance nodes
    queue = PriorityQueue()
    queue.put([0, start])

    # Distance and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = defaultdict(list)

    while not queue.empty():
        current_distance, current_node = queue.get()
        print(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = [current_node]  # Clear and add new predecessor
                queue.put([distance, neighbor])
            elif distance == distances[neighbor]:
                predecessors[neighbor].append(current_node)  # Add another path

    return distances, predecessors

def reconstruct_paths(predecessors, target):
    paths = []

    def backtrack(path, node):
        if not predecessors[node]:
            paths.append(path[::-1])  # Add reversed path
            return
        for pred in predecessors[node]:
            backtrack(path + [pred], pred)

    backtrack([], target)
    return paths

# Example usage
graph = {
    'A': {'B': 1, 'C': 1},
    'B': {'C': 1, 'D': 1},
    'C': {'D': 1},
    'D': {}
}
distances, predecessors = dijkstra_all_paths(graph, 'A')
all_paths = reconstruct_paths(predecessors, 'D')
print(all_paths)  # Output all shortest paths from A to D
