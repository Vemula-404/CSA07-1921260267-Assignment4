# Bill of Materials – Outpatient Block

| Item | Spec | Qty | Note |
|---|---|---|---|
| Access switch | 24×1G + 4 SFP | 2 | one per floor |
| Distribution switch | L3, 24×SFP + 8×10G | 1 | inter-VLAN routing |
| Wi-Fi 6 AP | 802.11ax PoE | 6 | hall, consulting, pharmacy |
| Firewall | NGFW 1 Gbps | 1 | clinical↔admin |
| Cat6 UTP | plenum | ~1,320 m | runs + 10% spare |
| Cat6A S/FTP | shielded | ~110 m | pharmacy 96 m + spare |
| OM4 fibre | LC-LC | ~460 m | 420 m + 10% |
| RJ45 keystone | Cat6/6A | ~80 | 2 per run + spare |
| Patch panel | 24-port Cat6 | 2 | one per TR |
| Rack | 12U wall-mount | 2 | one per TR |

**Collision domains:** one per switch port.
**Broadcast domains:** one per VLAN → 3 VLANs × 5 blocks = 15 + WAN = 16.