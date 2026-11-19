LIMIT = 90  # m permanent link (TIA/EIA-568)

runs = [
    ("Consulting rooms", 80,  "Cat6 UTP"),
    ("Pharmacy",         96,  "Cat6A S/FTP"),
    ("Waiting-hall APs", 60,  "Cat6 UTP"),
    ("Main-building link", 420, "OM4 multimode fibre"),
]

for name, dist, medium in runs:
    status = "OK" if dist <= LIMIT else "EXCEEDS 90 m"
    print(f"{name:22s} {dist:4d} m  {status:14s} -> {medium}")