# Trust Zones and Segmentation

This assessment evaluates the security posture of the Festo Smart Factory Lab OT/ICS network. The lab comprises six manufacturing stations (conveyor, sorting, camera inspection, magazine, press, oven) plus a robot arm cell, interconnected through Siemens S7-1500 PLCs, Festo CPX controllers, MTP700 HMIs, and a centralised MES PC.

The assessment is based on passive packet capture analysis (5 captures, ~55,000 frames), active DCP Identify-All output (14 devices), and nmap host discovery (21 live hosts across 172.21.0.0/18).

| Assessment Scope             | Key Finding                                     |
|:-----------------------------|:------------------------------------------------|
| Network segmentation         | NONE — fully flat /18 subnet                    |
| PLC access control           | NONE — all PLCs reachable from any host         |
| MES / OT separation          | NONE — MES PC shares subnet with PLCs           |
| Engineering access control   | NONE — uncontrolled, incl. unregistered devices |
| Unaccounted assets           | 6+ devices not in original inventory            |
| Wireless / external exposure | TP-Link AP present on OT subnet                 |