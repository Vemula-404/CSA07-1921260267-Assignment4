# Task 4 – Multiple Access, WLAN, WAN

## Multiple Access
- Pure ALOHA Smax ≈ 18.4% (G=0.5)
- Slotted ALOHA Smax ≈ 36.8% (G=1)
- 10 Mbps / 2,500 m CSMA/CD: 2τ = 25 µs → 250 bits min → rounded to **64 bytes**

**Switched full-duplex** = no contention → no CSMA/CD.
**Wi-Fi** = shared half-duplex → CSMA/CA + RTS/CTS (hidden node).

## WLAN (300 phones)
~50 active phones/AP → **6 APs**.
2.4 GHz channels: 1,6,11,1,6,11.
5 GHz non-overlapping: 36,40,44,48,149,153,157,161.

Wi-Fi 6: OFDMA (resource units), MU-MIMO (spatial streams), BSS colouring (dense halls).
Bluetooth good: low-power wearables/sensors. Bad: video, imaging, low-latency.

## WAN
ATM overhead = 5/53 ≈ 9.4% vs Ethernet ≈ 1.19%.
VC IDs: Frame Relay DLCI (10-bit), ATM VPI/VCI (5-byte header), MPLS 20-bit label.

**MPLS chosen** over Internet VPN for 3 clinics: SLA bandwidth, low jitter, native QoS for video consults. Accept up to ~40–50% premium.