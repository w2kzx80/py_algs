
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
# возвращал список вершин, которые необходимо обойти.

import random

def generate_graph(n):
    graph=[]
    for i in range(n):
        ga = []
        for k in range(n):
            if k != i and random.random() > 0.5:
                ga.append(random.randint(1,10))
            else:
                ga.append(0)
        graph.append(ga)
    return graph

graph = generate_graph(7)
graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]
print(*graph, sep="\n")
print("="*50)

s=int(input("Номер изначальной вершины? (начиная с 0)"))

def dekstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    puti = []
    for i in range(length):
        puti.append([])
        k = i
        while parent[k]!=-1:
            puti[i].append(parent[k])
            k = parent[k]
        puti[i] = puti[i][::-1]
        if len(puti[i])>0:
            puti[i].append(i)
    return cost, puti

print(dekstra(graph, s))