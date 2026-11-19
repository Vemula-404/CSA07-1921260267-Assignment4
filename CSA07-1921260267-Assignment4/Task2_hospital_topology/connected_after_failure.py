def connected_after_failure(edges, n, broken):
    adj = {i: [] for i in range(n)}
    adj['hub'] = []
    for e in edges:
        if e == broken:
            continue
        a, b = e
        adj[a].append(b)
        adj[b].append(a)

    visited = set()
    queue = [0]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for nb in adj.get(node, []):
            if nb not in visited:
                queue.append(nb)

    return all(i in visited for i in range(n))


if __name__ == "__main__":
    n = 5
    bus  = [(0,1),(1,2),(2,3),(3,4)]
    ring = [(0,1),(1,2),(2,3),(3,4),(4,0)]
    star = [(0,1),(0,2),(0,3),(0,4)]
    mesh = [(i,j) for i in range(n) for j in range(i+1,n)]

    for name, edges in [("bus",bus),("ring",ring),("star",star),("mesh",mesh)]:
        survive = sum(connected_after_failure(edges, n, e) for e in edges)
        print(f"{name}: {survive}/{len(edges)}")