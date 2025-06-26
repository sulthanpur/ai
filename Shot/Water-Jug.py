# def water_jug(a, b, target, jugA=0, jugB=0, visited=None):
#     if visited is None:
#         visited = set()
#     if (jugA, jugB) in visited:
#         return
#     visited.add((jugA, jugB))

#     print(f"JugA: {jugA}, JugB: {jugB}")

#     if jugA == target or jugB == target:
#         print("Target reached!")
#         return

#     if jugA == 0:
#         water_jug(a, b, target, a, jugB, visited)           # Fill Jug A
#     elif jugB != b:
#         pour = min(jugA, b - jugB)
#         water_jug(a, b, target, jugA - pour, jugB + pour, visited)  # Pour A -> B
#     else:
#         water_jug(a, b, target, 0, jugB, visited)           # Empty Jug A

# water_jug(4, 3, 2)



def water_jug(a, b, target, jugA=0, jugB=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    if (jugA, jugB) in visited:
        return
    
    visited.add((jugA, jugB))
    path.append((jugA, jugB))

    if jugA == target or jugB == target:
        print("Steps to reach target:")
        for step in path:
            print(f"JugA: {step[0]}, JugB: {step[1]}")
        print("Target reached!\n")
        path.pop()
        return

    # All 6 operations
    # Fill Jug A
    water_jug(a, b, target, a, jugB, visited.copy(), path.copy())

    # Fill Jug B
    water_jug(a, b, target, jugA, b, visited.copy(), path.copy())

    # Empty Jug A
    water_jug(a, b, target, 0, jugB, visited.copy(), path.copy())

    # Empty Jug B
    water_jug(a, b, target, jugA, 0, visited.copy(), path.copy())

    # Pour A → B
    pour = min(jugA, b - jugB)
    water_jug(a, b, target, jugA - pour, jugB + pour, visited.copy(), path.copy())

    # Pour B → A
    pour = min(jugB, a - jugA)
    water_jug(a, b, target, jugA + pour, jugB - pour, visited.copy(), path.copy())

    path.pop()

# Run for example:
water_jug(4, 3, 2)
