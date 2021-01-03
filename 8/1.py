
# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

def generate_graph(n):
    graph=[]
    for i in range(n-1):
        ga = []
        for k in range(i+1,n):
            ga.append(k)
        graph.append(ga)
    return graph

graph = generate_graph(7)
print(f"Итого {sum([len(i) for i in graph])} рукопожатий")