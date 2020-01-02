# Breadth First Search algorithm
# Autor: Leonardo Tada

from queue import Queue

graph = [[1,1,1,1],
         [0,1,1,0],
         [0,1,0,1],
         [0,1,9,1],
         [1,1,1,1]];


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.x == other.x) and (self.y == other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))



def neighbors(current):
    result = []
    x = current.x
    y = current.y
    nodes_to_test = [Node(x, y+1), Node(x, y-1), Node(x+1, y), Node(x-1, y)]
    for node in nodes_to_test:
        print(node.y, node.x)
        # verify map bounds
        if ((node.x < 0) or
           (node.y < 0) or
           (node.y > len(graph)-1) or
           (node.x > len(graph[0])-1)):
            continue
        try:
            if graph[node.y][node.x] == 1 or graph[node.y][node.x] == 9:
                result.append(node)
        except IndexError:
            pass
    return result


def main():
    start = Node(0, 0)
    goal = Node(2, 3)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    # generate path
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    result_path = [(node.x, node.y) for node in path]
    print(result_path)


if __name__ == '__main__':
    main()
