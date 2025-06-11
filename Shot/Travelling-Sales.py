from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
min_cost = float('inf')
min_path = []

for perm in permutations(range(1, n)):
    cost = graph[0][perm[0]]
    for i in range(len(perm) - 1):
        cost += graph[perm[i]][perm[i+1]]
    cost += graph[perm[-1]][0]
    if cost < min_cost:
        min_cost = cost
        min_path = [0] + list(perm) + [0]

print("Minimum cost:", min_cost)
print("Path:", min_path)