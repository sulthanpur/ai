def tsp_bfs(graph):
    n = len(graph)  # Number of cities
    startCity = 0
    min_cost = float('inf')
    opt_path = []

    # Use regular list as a queue for BFS
    queue = [([startCity], 0)]

    print("Path Traversal:")

    while queue:

        print("\n the Que : ",queue,"\n")
        cur_path, cur_cost = queue.pop(0)  # FIFO behavior

       

        print("cur_path ",cur_path,"cur_cost ",cur_cost)

        cur_city = cur_path[-1]

        # Show current path and cost
        print(f"Current Path: {cur_path}, Current Cost: {cur_cost}")

        # If all cities are visited and we return to start
        if len(cur_path) == n and cur_path[0] == startCity:

            print("current Path inside : ",cur_path)

            total_cost = cur_cost + graph[cur_city][startCity]
            if total_cost < min_cost:
                min_cost = total_cost
                opt_path = cur_path + [startCity]
            continue

        # Explore next cities
        for next_city in range(n):
            if next_city not in cur_path:
                new_path = cur_path + [next_city]
                print("new_path ",new_path)
                new_cost = cur_cost + graph[cur_city][next_city]
                queue.append((new_path, new_cost))

    return min_cost, opt_path


# Example graph (adjacency matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Run the TSP solver
min_cost, opt_path = tsp_bfs(graph)

print("\nOptimal Solution:")
print(f"Minimum cost: {min_cost}")
print(f"Optimal path: {opt_path}")
