from collections import defaultdict


def bfs(n, m, edges, s):
    myDict = defaultdict(int)
    queue = list()

    for node in range(1, n + 1):
        myDict[node] = []

    for edge in edges:
        myDict[edge[0]].append(edge[1])
        myDict[edge[1]].append(edge[0])

    leng = len(myDict.keys()) + 1
    distances = [-1]*leng
    queue.append(s)
    distances[s] = 0

    while len(queue) > 0:
        current = queue.pop(0)
        for nb in myDict[current]:
            if distances[nb] == -1:
                distances[nb] = distances[current] + 6
                queue.append(nb)

    distances.pop(s)
    distances.pop(0)
    return distances

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())
        result = bfs(n, m, edges, s)
        print(result)
