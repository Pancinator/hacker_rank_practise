
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.visited = False

    def add_neighbour(self, node):
        self.neighbours.append(node)


class Graph:
    nodes = {}

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        else:
            return False

    def add_edge(self, node_u, node_v):
        if node_u.name in self.nodes and node_v.name in self.nodes:
            for key, value in self.nodes.items():
                if key == node_u.name:
                    value.add_neighbour(node_v)
                if key == node_v.name:
                    value.add_neighbour(node_u)
            return True
        else:
            return False

    def print_graph(self):
        for key in self.nodes.keys():
            print(str(key) + str([nb.name for nb in self.nodes[key].neighbours]) + " ")

    #BFS graph traversal, print all nodes in graph
    def bfs_traversal(self, node):
        queue = list()
        visited = list()
        visited.append(node.name)

        for nb in node.neighbours:
            queue.append(nb)
        print(visited)
        while len(queue) > 0:
            print('visited:')
            print(visited)
            print('queueu' + str([node.name for node in queue]))
            node_u = queue.pop(0)
            print("popped node:" + str(node_u.name))
            #visited.append(node_u.name)
            for v in node_u.neighbours:
                if v.name not in visited:
                    queue.append(v)
                    visited.append(v.name)
        return sorted(visited)

    #find the shortest path in graph with BFS
    def bfs_shortest_path(self, start_node, dest_node):
        queue = list()
        leng = len(self.nodes.keys())
        distances = [-1]*leng
        queue.append(start_node)
        distances[start_node.name] = 0

        while len(queue) > 0:

            current = queue.pop(0)
            print('current: ' + str(current.name))
            for nb in current.neighbours:
                if distances[nb.name] == -1:
                    distances[nb.name] = distances[current.name] + 1
                    queue.append(nb)

        return distances[dest_node.name]



node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

graph = Graph()
graph.add_node(node0)
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
graph.add_node(node5)
graph.add_node(node6)
graph.add_node(node7)
graph.add_node(node8)

graph.add_edge(node0, node1)
graph.add_edge(node1, node2)
graph.add_edge(node1, node4)
graph.add_edge(node4, node3)
graph.add_edge(node2, node3)
graph.add_edge(node3, node8)
graph.add_edge(node8, node7)
graph.add_edge(node3, node7)
graph.add_edge(node7, node6)
graph.add_edge(node6, node5)
graph.add_edge(node5, node4)

graph.print_graph()
print(graph.bfs_traversal(node0))
print('BFS:')
print(graph.bfs_shortest_path(node0, node8))
