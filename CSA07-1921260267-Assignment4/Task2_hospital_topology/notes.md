# Task 2 – Hospital Topology

| Topology | Links | Ports | Cost (Rs) | Single-cut survives? |
|---|---|---|---|---|
| Bus | 4 | 8 | 3,84,000 | No |
| Ring | 5 | 10 | 4,80,000 | Yes |
| Star | 5 | 6 | 4,08,000 | No |
| Full Mesh | 10 | 20 | 9,60,000 | Yes |

**Chosen: Hybrid** – triangle Emergency–Theatres–Admin + leaves Lab & Outpatient on Admin.
Core = 5 links, 10 ports → Rs 4,80,000. Cheaper than mesh, meets rule for critical blocks.

**n=20 scaling:** Star = 20 links; Mesh = 190 links → Rs 1.14 crore cable. Mesh grows quadratically.

**Ring vs Hybrid:** both survive single cut; hybrid easier to expand (re-home leaves without re-planning ring).