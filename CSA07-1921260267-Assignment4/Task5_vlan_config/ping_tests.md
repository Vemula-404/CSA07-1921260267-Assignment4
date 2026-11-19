# Task 5 – Ping Results from VLAN-30 Guest PC

| Destination | VLAN | Result |
|---|---|---|
| 8.8.8.8 | WAN | Reply — permitted |
| 192.168.10.10 (Office) | 10 | Timed out — denied |
| 192.168.20.10 (CCTV) | 20 | Timed out — denied |
| 192.168.10.1 (VLAN10 gw) | 10 | Timed out — denied |

**802.1Q overhead:** +4 bytes (TPID 0x8100 + TCI) → 1518 → 1522 bytes ≈ **0.26%**.

**Broadcast domains:** before = 1; after = 3 (one per VLAN).

**VLAN vs Physical separation:** VLAN = zero extra hardware. Physical separation only for compliance (PCI-DSS, HIPAA).