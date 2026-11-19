# Task 6 – Campus Design

## Stage 1 – Requirements
| Building | Users/Devices | Peak |
|---|---|---|
| Academic | 2000 wired + 1500 wireless | 3G wired + 1G wireless |
| Labs | 600 wired | ~6 Gbps |
| Library | 300 wired + 500 wireless | 2 Gbps |
| Hostels | 3000 wireless | 3 Gbps |
| Auditorium | 1000 wireless | 2 Gbps |
| Data centre | servers/storage | 20 Gbps |

Testable: ≥100 Mbps/device, ≥4 VLANs, single-link failover, dual-ISP failover <30s, 20% growth headroom.

## Stage 2 – Topology
Hierarchical hybrid: **Core (2×L3 VPC) → Distribution (per building, dual-homed) → Access (star)**.
Dual ISP with BGP.

## Stage 3 – Decisions
- Devices: L3 core/dist, L2 access + PoE, NGFW, Wi-Fi 6 APs
- Media: SMF backbone, Cat6A S/FTP building runs, Cat6 drops
- VLANs: Student, Staff, Guest, CCTV, Mgmt
- WLAN: 802.11ax, WPA3-Enterprise, controller-managed
- WAN: dual 1 Gbps ISP + BGP + SD-WAN

## Stage 4 – Address & Oversubscription
(see ip_plan.csv and oversubscription.py — 2:1 at access→distribution)

## Stage 5 – Security / Growth
- Firewall at ISP edge + between VLANs
- 802.1X for staff/student, captive portal for guest
- Backbone SMF supports 40/100G upgrade without re-cabling