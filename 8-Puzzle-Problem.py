from collections import deque

def bfs(start_state):
    target = [1, 2, 3, 4, 5, 6, 7, 8 , 0]
    dq = deque([start_state])
    visited = {tuple(start_state): None}

    while dq:
        state = dq.popleft()
        if state == target:
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)
        for move in (-3, 3, -1, 1):
            new_row, new_col = divmod(zero + move, 3)
            if 0 <= new_row < 3 and 0 <= new_col < 3 and abs(row - new_row) + abs(col - new_col) == 1:
                neighbor = state[:]
                neighbor[zero], neighbor[zero + move] = neighbor[zero + move], neighbor[zero]
                if tuple(neighbor) not in visited:
                    visited[tuple(neighbor)] = state
                    dq.append(neighbor)

def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")

# Example Usage
startState = [1, 3, 0 , 6, 8, 4, 7, 5, 2]
solution = bfs(startState)
if solution:
    printSolution(solution)
    print(f"Solved in {len(solution) - 1} moves.")
else:
    print("No solution found.")



### OUTPUT ###


# 1 3 0
# 6 8 4
# 7 5 2
# -----
# 1 3 4
# 6 8 0
# 7 5 2
# -----
# 1 3 4
# 6 8 2
# 7 5 0
# -----
# 1 3 4
# 6 8 2
# 7 0 5
# -----
# .
# .
# .
# -----
# 1 2 3
# 4 5 0
# 7 8 6
# -----
# 1 2 3
# 4 5 6
# 7 8 0
# -----
# Solved in 20 moves.






# def bfs(start_state):
#     target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#     queue = [start_state]
#     visited = {tuple(start_state): None}

#     while queue:
#         state = queue.pop(0)
#         if state == target:
#             path = []
#             while state:
#                 path.append(state)
#                 state = visited[tuple(state)]
#             return path[::-1]

#         zero = state.index(0)
#         row = zero // 3
#         col = zero % 3

#         for move in [-3, 3, -1, 1]:
#             new_pos = zero + move
#             if 0 <= new_pos < 9:
#                 new_row = new_pos // 3
#                 new_col = new_pos % 3

#                 if abs(row - new_row) + abs(col - new_col) == 1:
#                     neighbor = []
#                     for value in state:
#                         neighbor.append(value)
#                     neighbor[zero], neighbor[new_pos] = neighbor[new_pos], neighbor[zero]

#                     if tuple(neighbor) not in visited:
#                         visited[tuple(neighbor)] = state
#                         queue.append(neighbor)

#     return None

# def printSolution(path):
#     for state in path:
#         for i in range(0, 9, 3):
#             print(state[i], state[i+1], state[i+2])
#         print("-----")

# # Example Usage
# startState = [1, 3, 0, 6, 8, 4, 7, 5, 2]
# solution = bfs(startState)
# if solution:
#     printSolution(solution)
#     print("Solved in", len(solution) - 1, "moves.")
# else:
#     print("No solution found.")
