CABLE = 60000
PORT  = 18000
n = 5

def cost(links, ports):
    return links * CABLE + ports * PORT

print("Bus   :", cost(4, 8))
print("Ring  :", cost(5, 10))
print("Star  :", cost(5, 6))
print("Mesh  :", cost(n*(n-1)//2, n*(n-1)))
print("Hybrid:", cost(5, 10))

# Scaling check for n=20
print("\nn=20:")
print("Star links:", 20, " Mesh links:", 20*19//2)
print("Mesh cable cost: Rs", (20*19//2)*CABLE)
print("Star cable cost: Rs", 20*CABLE)