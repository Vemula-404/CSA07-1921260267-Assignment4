import math

print(f"Pure ALOHA Smax = 1/(2e) = {1/(2*math.e):.4f} = {100/(2*math.e):.1f}%")
print(f"Slotted ALOHA Smax = 1/e = {1/math.e:.4f} = {100/math.e:.1f}%")

dist = 2500
speed = 2e8
rate = 10e6
tau = dist/speed
min_bits = rate * 2 * tau
print(f"tau = {tau*1e6:.1f} us, 2*tau = {2*tau*1e6:.1f} us")
print(f"Min frame = {min_bits:.0f} bits = {min_bits/8:.2f} bytes -> standard rounds to 64 bytes")