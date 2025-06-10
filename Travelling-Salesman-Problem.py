from collections import deque

def tsp_bfs(graph):
    n = len(graph)  # Number of cities
    startCity = 0       # Starting city
    min_cost = float('inf')  # Initialize minimum cost as infinity
    opt_path = []        # To store the optimal path
    
    # Queue for BFS: Each element is (cur_path, cur_cost)
    dq = deque([([startCity], 0)])  
    
    print("Path Traversal:")
    
    while dq:
        cur_path, cur_cost = dq.popleft()
        cur_city = cur_path[-1]
        
        # Print the current path and cost
        print(f"Current Path: {cur_path}, Current Cost: {cur_cost}")
        
        # If all cities are visited and we are back at the startCity
        if len(cur_path) == n and cur_path[0] == startCity:
            total_cost = cur_cost + graph[cur_city][startCity]
            if total_cost < min_cost:
                min_cost = total_cost
                opt_path = cur_path + [startCity]
            continue
        
        # Explore all neighboring cities (add in BFS manner)
        for next_city in range(n):
            if next_city not in cur_path:  # Visit unvisited cities
                new_path = cur_path + [next_city]
                new_cost = cur_cost + graph[cur_city][next_city]
                dq.append((new_path, new_cost))
    
    return min_cost, opt_path

# Example graph as a 2D adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve TSP using BFS
min_cost, opt_path = tsp_bfs(graph)

print("\nOptimal Solution:")
print(f"Minimum cost: {min_cost}")
print(f"Optimal path: {opt_path}")



###  OUTPUT  ###

# Path Traversal:
# Current Path: [0], Current Cost: 0
# Current Path: [0, 1], Current Cost: 10
# Current Path: [0, 2], Current Cost: 15
# Current Path: [0, 3], Current Cost: 20
# Current Path: [0, 1, 2], Current Cost: 45
# Current Path: [0, 1, 3], Current Cost: 35
# Current Path: [0, 2, 1], Current Cost: 50
# Current Path: [0, 2, 3], Current Cost: 45
# Current Path: [0, 3, 1], Current Cost: 45
# Current Path: [0, 3, 2], Current Cost: 50
# Current Path: [0, 1, 2, 3], Current Cost: 75
# Current Path: [0, 1, 3, 2], Current Cost: 65
# Current Path: [0, 2, 1, 3], Current Cost: 75
# Current Path: [0, 2, 3, 1], Current Cost: 70
# Current Path: [0, 3, 1, 2], Current Cost: 80
# Current Path: [0, 3, 2, 1], Current Cost: 85

# Optimal Solution:
# Minimum cost: 80
# Optimal path: [0, 1, 3, 2, 0]