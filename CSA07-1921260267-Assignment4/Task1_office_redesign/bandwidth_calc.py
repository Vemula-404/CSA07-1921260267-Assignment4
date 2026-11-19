# Bus+Hub vs switched star: bandwidth per device
devices = 33          # 30 PCs + hub + server + printer
bus_rate = 10         # Mbps shared

per_device_bus = bus_rate / devices
print(f"Bus: {bus_rate} Mbps shared / {devices} = {per_device_bus:.2f} Mbps per device (best case)")
print("Switched star: 1000 Mbps dedicated full-duplex per port")

# Collision domain count
print(f"Bus collision domains: 1")
print(f"Star collision domains: {devices} (one per switch port)")