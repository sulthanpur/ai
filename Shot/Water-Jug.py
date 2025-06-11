def water_jug(a, b, target, jugA=0, jugB=0, visited=None):
    if visited is None:
        visited = set()
    if (jugA, jugB) in visited:
        return
    visited.add((jugA, jugB))

    print(f"JugA: {jugA}, JugB: {jugB}")

    if jugA == target or jugB == target:
        print("Target reached!")
        return

    if jugA == 0:
        water_jug(a, b, target, a, jugB, visited)           # Fill Jug A
    elif jugB != b:
        pour = min(jugA, b - jugB)
        water_jug(a, b, target, jugA - pour, jugB + pour, visited)  # Pour A -> B
    else:
        water_jug(a, b, target, 0, jugB, visited)           # Empty Jug A

water_jug(4, 3, 2)