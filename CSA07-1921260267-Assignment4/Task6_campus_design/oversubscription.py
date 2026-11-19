links = [
    ("Academic access -> distribution", 20, 10),   # 2x10G LAG, 10G uplink
    ("Labs access -> distribution",     40, 20),   # 4x10G LAG, 20G uplink
]
for name, access, uplink in links:
    print(f"{name}: access {access} Gbps / uplink {uplink} Gbps = {access/uplink:.0f}:1")