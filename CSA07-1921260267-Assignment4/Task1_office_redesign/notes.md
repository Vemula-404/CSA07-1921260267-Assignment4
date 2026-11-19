# Task 1 – Office Redesign

## Complaints → Causes
1. Desk move kills network → single coax bus, shared medium.
2. Month-end slow → one 10 Mbps collision domain (~0.31 Mbps/device).
3. Router restart kills internet → single gateway, no separation.

## Redesign
Extended star: Firewall/Router → Core switch → Floor-2 switch (fibre) → PCs, server, printer on Cat6.

| Metric | Before | After |
|---|---|---|
| Shared medium | 10 Mbps bus, 33 devices | 1 Gbps per port |
| Per computer | ~0.31 Mbps | 1000 Mbps full-duplex |
| Collision domains | 1 | 1 per port |
| Desk move impact | whole office | one port |

## Verdict
Switched star fixes all three complaints. All-Wireless (Wi-Fi 6) is cheaper but shared medium / CSMA/CA contention fails month-end file saving → keep wired star for desktops.