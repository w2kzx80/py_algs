
# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).

import random

def generate_graph(n):
    graph=[]
    for i in range(n):
        ga = [int(i) for i in input(f"Cвязи вершины {i} через пробел:").split()]
        graph.append(ga)
    return graph

graph = generate_graph(6)
print(*graph, sep="\n")
print("="*50)

def go(graph):
    current = 0
    is_visited = [False] * len(graph)
    parents = []

    found = True
    while found:
        if not is_visited[current]:
            print(current)
            is_visited[current] = True

        for i in graph[current]:
            if found == False and is_visited[i] == False:
                parents.push(current)
                current = graph[current]
                found = True

        if not found:
            if len(parents)>0:
                current = parents.pop()

go(graph)