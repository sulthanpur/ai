# def tsp_bfs(graph):
#     n = len(graph)  # Number of cities
#     startCity = 0
#     min_cost = float('inf')
#     opt_path = []

#     # Use regular list as a queue for BFS
#     queue = [([startCity], 0)]

#     print("Path Traversal:")

#     while queue:

#         print("\n the Que : ",queue,"\n")
#         cur_path, cur_cost = queue.pop(0)  # FIFO behavior

       

#         print("cur_path ",cur_path,"cur_cost ",cur_cost)

#         cur_city = cur_path[-1]

#         # Show current path and cost
#         print(f"Current Path: {cur_path}, Current Cost: {cur_cost}")

#         # If all cities are visited and we return to start
#         if len(cur_path) == n and cur_path[0] == startCity:

#             print("current Path inside : ",cur_path)

#             total_cost = cur_cost + graph[cur_city][startCity]
#             if total_cost < min_cost:
#                 min_cost = total_cost
#                 opt_path = cur_path + [startCity]
#             continue

#         # Explore next cities
#         for next_city in range(n):
#             if next_city not in cur_path:
#                 new_path = cur_path + [next_city]
#                 print("new_path ",new_path)
#                 new_cost = cur_cost + graph[cur_city][next_city]
#                 queue.append((new_path, new_cost))

#     return min_cost, opt_path


# # Example graph (adjacency matrix)
# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# # Run the TSP solver
# min_cost, opt_path = tsp_bfs(graph)

# print("\nOptimal Solution:")
# print(f"Minimum cost: {min_cost}")
# print(f"Optimal path: {opt_path}")








# Distance matrix
distance = [
    [0, 10, 15, 20],  # From city 0
    [10, 0, 35, 25],  # From city 1
    [15, 35, 0, 30],  # From city 2
    [20, 25, 30, 0]   # From city 3
]

n = len(distance)  # Number of cities
min_cost = float('inf')
best_path = []

# Function to generate permutations
def permute(path, l, r):
    global min_cost, best_path
    if l == r:
        cost = 0
        full_path = [0] + path + [0]  # Start and end at city 0
        for i in range(len(full_path) - 1):
            cost += distance[full_path[i]][full_path[i+1]]
        if cost < min_cost:
            min_cost = cost
            best_path = full_path[:]
    else:
        for i in range(l, r+1):
            path[l], path[i] = path[i], path[l]  # swap
            permute(path, l+1, r)
            path[l], path[i] = path[i], path[l]  # backtrack

# Start from city 0, so generate permutations of cities 1 to n-1
cities = []
for i in range(1, n):
    cities.append(i)

# Call our custom permutation function
permute(cities, 0, len(cities)-1)

# Print result
print("Best path:", ' -> '.join(str(city) for city in best_path))
print("Minimum cost:", min_cost)

