# Asset Inventory

---

## Infrastructure / Level 0 Network

| Asset                   | Type               | Model / Firmware           | IP                          | MAC                                   | Available Protocols   | Function                                               |
|-------------------------|--------------------|----------------------------|-----------------------------|---------------------------------------|-----------------------|--------------------------------------------------------|
| Gateway                 | Router / Firewall  | ?                          | 172.21.0.230                | ?                                     | Ethernet              | Network gateway for all stations                       |
| festo-mes-pc            | MES PC             | SIMATIC-PC                 | 172.21.0.90                 | 4c:d7:17:90:73:a2                     | PROFINET / Ethernet   | MES / NTP Server                                       |
| desktop-6jd9ili         | Engineering PC     | SIMATIC-PC                 | 172.21.0.168 / 172.21.0.192 | 02:1b:1b:29:49:00 / 08:26:ae:3e:a5:ad | Ethernet              | Dual-NIC engineering/admin station                     |
| gebruik-tt8ke80         | Physical NIC       | SIMATIC-PC                 | 172.21.0.165                | 60:cf:84:d1:d0:d5                     | Ethernet              | VMWare Virtualisation Host                             |
| gebruik-tt8ke80         | VMWare Virtual NIC | VMWare                     | 172.21.0.165                | 00:0c:29:63:ba:59                     | ?                     | VMWare Virtual NIC                                     |
| CPX-IOT                 | MQTT Broker?       | Festo                      | 172.21.0.210                | 00:0E:F0:7C:A3:C0                     | ?                     | ?                                                      |
| Engineering Workstation | Engineering PC     | ?                          | 172.21.0.156                | c4:c6:e6:d4:c3:81                     | S7comm, SSDP M-SEARCH | Engineering station connecting to PLC S2 (TIA Portal?) |
| Smart Switch            | Switch             | Netgear GS305E / V1.0.0.16 | 172.21.0.196                | 28:94:01:67:5b:8b                     | ?                     | ?                                                      |
| Router or AP            | Router             | TP-Link router             | 172.21.0.200                | 20:23:51:41:a2:88                     | UDP                   | Router?                                                |

---

## Station 0 – Robot Arm (172.21.0.x)

| Asset        | Type        | Model / Firmware          | IP              | MAC               | Available Protocols | Function                       |
|--------------|-------------|---------------------------|-----------------|-------------------|---------------------|--------------------------------|
| Robot Arm    | Robot       | Universal Robots UR3e / ? | 172.21.1.40     | ?                 | UR Bus / Ethernet   | Pick & place cobot             |
| Switch S0    | Switch      | Siemens Scalance XB008    | N/A (unmanaged) | N/A (unmanaged)   | Ethernet            | Station 0 network distribution |
| rfidboxcobot | RFID Reader | Turck TBEN-S2-2RFID-4DXP  | 172.21.1.20     | 00:07:46:aa:07:cc | PROFINET            | RFID identification near cobot |

### Switch S0 – Port Connections

| Port | Connected To     |
|------|------------------|
| P1   | Connector pinout |
| P2   | —                |
| P3   | —                |
| P4   | Station 2 HMI    |
| P5   | UR extension bus |
| P6   | —                |
| P7   | —                |
| P8   | —                |

---

## Station 1 – Conveyor Belt (172.21.1.x)

| Asset       | Type   | Model / Firmware                                              | IP              | MAC               | Available Protocols            | Function                                   |
|-------------|--------|---------------------------------------------------------------|-----------------|-------------------|--------------------------------|--------------------------------------------|
| Switch S1   | Switch | Siemens Scalance XB008                                        | N/A (unmanaged) | N/A (unmanaged)   | Ethernet                       | Station 1 network distribution             |
| HMI S1?     | HMI    | Siemens MTP700 Unified Comfort                                | 172.21.1.10     | 30:13:89:35:da:a8 | PROFINET                       | Operator panel — confirm station ownership |
| PLC S1      | PLC    | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3 | 172.21.1.1      | 30:B8:51:32:D3:E7 | PROFINET, HTTP, OPC-UA, S7comm | Process control S1                         |
| PC Cobot-ML | PC     | ?                                                             | 172.21.1.90     | 08:bf:b8:f1:25:e3 | OPC-UA                         | ?                                          |

### Switch S1 – Port Connections

| Port | Connected To  |
|------|---------------|
| P1   | —             |
| P2   | Switch S2     |
| P3   | Station 2 HMI |
| P4   | —             |
| P5   | —             |
| P6   | —             |
| P7   | —             |
| P8   | —             |

---

## Station 2 – Ball Sorting / Dispense (172.21.2.x)

| Asset                          | Type       | Model / Firmware                                                         | IP              | MAC                                                  | Available Protocols            | Function                             |
|--------------------------------|------------|--------------------------------------------------------------------------|-----------------|------------------------------------------------------|--------------------------------|--------------------------------------|
| PLC S2                         | PLC        | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3            | 172.21.2.1      | 30:b8:51:33:7e:c7                                    | PROFINET, HTTP, OPC-UA, S7comm | Process control S2                   |
| HMI S2                         | HMI        | Siemens MTP700 Unified Comfort                                           | 172.21.2.10     | 30:13:89:35:d8:af                                    | PROFINET                       | Operator panel (`hmixbdispense`)     |
| Switch S2                      | Switch     | Siemens Scalance XB008                                                   | N/A (unmanaged) | N/A (unmanaged)                                      | Ethernet                       | Station 2 network distribution       |
| CPX Programmable Controller S2 | Controller | Siemens                                                                  | 172.21.2.60     | 00:0E:F0:99:CB:38                                    | ?                              | Controller for industrial automation |
| Power Monitor S2               | Monitor    | Siemens                                                                  | 172.21.2.61     | 10:DF:FC:17:DC:72                                    | ?                              | Power consumption monitoring         |
| IO Device                      | IO Device  | Siemens ET200SP IM155-6PN/2 HF, 6ES7 155-6AU01-0CN0 / V4.2.4, HW: V4.0.0 | 172.21.2.100    | Port A: 4c:e7:05:4b:46:4b, Port B: 4c:e7:05:4b:46:4c | PROFINET IO                    | Remote IO Module                     |

### Switch S2 – Port Connections

| Port | Connected To                 |
|------|------------------------------|
| P1   | Switch S1                    |
| P2   | Switch S3                    |
| P3   | PLC front (→ SCALANCE XB008) |
| P4   | IO Device                    |
| P5   | —                            |
| P6   | Power Monitor                |
| P7   | Switch S0                    |
| P8   | PC Cobot-ML (172.21.1.90)    |

---

## Station 3 – Camera Inspection (172.21.3.x)

| Asset            | Type    | Model / Firmware                                              | IP              | MAC               | Available Protocols            | Function                              |
|------------------|---------|---------------------------------------------------------------|-----------------|-------------------|--------------------------------|---------------------------------------|
| PLC S3           | PLC     | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3 | 172.21.3.1      | 30:b8:51:32:d3:9b | PROFINET, HTTP, OPC-UA, S7comm | Process control S3 (`plcxbfesto62c9`) |
| HMI S3           | HMI     | Siemens MTP700 Unified Comfort                                | 172.21.3.10     | 30:13:89:2c:e9:c5 | PROFINET                       | Operator panel                        |
| Switch S3        | Switch  | Siemens Scalance XB008                                        | N/A (unmanaged) | N/A (unmanaged)   | Ethernet                       | Station 3 network distribution        |
| Sensor S3        | Sensor  | SensoPart / ?                                                 | 172.21.3.50     | 00:19:6F:0D:A3:72 | HTTP                           | Vision / inspection sensor            |
| Power Monitor S3 | Monitor | ?                                                             | ?               | ?                 | ?                              | Power consumption monitoring          |

### Switch S3 – Port Connections

| Port | Connected To                      |
|------|-----------------------------------|
| P1   | Switch S2                         |
| P2   | Switch S4                         |
| P3   | PLC front (→ SCALANCE XB008)      |
| P4   | Sensor                            |
| P5   | Upward / general switch (confirm) |
| P6   | Power Monitor                     |
| P7   | Switch S0                         |
| P8   | PC Cobot-ML / upward? (confirm)   |

---

## PLC Segment – Stations 2 & 3

| Asset          | Type          | Model / Firmware       | IP          | MAC               | Available Protocols | Function                     |
|----------------|---------------|------------------------|-------------|-------------------|---------------------|------------------------------|
| SCALANCE XB008 | Switch        | Siemens SCALANCE XB008 | N/A (unmanaged)         | N/A (unmanaged)                 | PROFINET            | PLC-side managed switch      |
| PC Cobot-ML    | Industrial PC | ?                      | 172.21.1.90 | 08:bf:b8:f1:25:e3 | Ethernet            | ML inference / cobot control |

### PLC Connections 

| Interface           | Connected To    |
|---------------------|-----------------|
| X1P3 (PROFINET LAN) | SCALANCE XB008  |
| HMI port            | pnl-L-HMI-T7-V2 |

---

## Station 4 – Magazine (172.21.4.x)

| Asset        | Type             | Model / Firmware                                              | IP              | MAC               | Available Protocols            | Function                          |
|--------------|------------------|---------------------------------------------------------------|-----------------|-------------------|--------------------------------|-----------------------------------|
| PLC S4       | PLC              | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3 | 172.21.4.1      | 30:b8:51:33:7e:24 | PROFINET, HTTP, OPC-UA, S7comm | Process control S4 (`plcmagback`) |
| HMI S4       | HMI              | Siemens MTP700 Unified Comfort                                | 172.21.4.10     | 30:13:89:35:D9:EF | PROFINET                       | Operator Panel                    |
| Switch S4    | Switch           | Siemens Scalance XB008                                        | N/A (unmanaged) | N/A (unmanaged)   | Ethernet                       | Station 4 network distribution    |
| CPX Terminal | Cloud I/O Device | Festo CPX (197330)                                            | ?               | ?                 | ?                              | Cloud-connected valve/IO terminal |

### Switch S4 – Port Connections

| Port | Connected To  |
|------|---------------|
| P1   | Station 3 HMI |
| P2   | PLC S4        |
| P3   | Switch S5     |
| P4   | —             |
| P5   | CPX Terminal  |
| P6   | —             |
| P7   | —             |
| P8   | —             |

---

## Station 5 – Muscle Press (172.21.5.x)

| Asset     | Type   | Model / Firmware                                              | IP              | MAC               | Available Protocols            | Function                             |
|-----------|--------|---------------------------------------------------------------|-----------------|-------------------|--------------------------------|--------------------------------------|
| PLC S5    | PLC    | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3 | 172.21.5.1      | 30:b8:51:33:7e:62 | PROFINET, HTTP, OPC-UA, S7comm | Process control S5 (`plcxamikea2a4`) |
| HMI S5    | HMI    | Siemens MTP700 Unified Comfort                                | 172.21.5.10     | 30:13:89:36:6A:EE | PROFINET                       | Operator Panel                       |
| Switch S5 | Switch | Siemens Scalance XB008                                        | N/A (unmanaged) | N/A (unmanaged)   | Ethernet                       | Station 5 network distribution       |

### Switch S5 – Port Connections

| Port | Connected To |
|------|--------------|
| P1   | Switch S4    |
| P2   | Switch S6    |
| P3   | PLC S5       |
| P4   | —            |
| P5   | —            |
| P6   | —            |
| P7   | —            |
| P8   | —            |

---

## Station 6 – Oven (172.21.6.x)

| Asset                          | Type       | Model / Firmware                                              | IP              | MAC               | Available Protocols            | Function                       |
|--------------------------------|------------|---------------------------------------------------------------|-----------------|-------------------|--------------------------------|--------------------------------|
| HMI S6                         | HMI        | Siemens MTP700 Unified Comfort                                | 172.21.6.10     | 30:13:89:35:d9:c7 | PROFINET                       | Operator panel                 |
| Switch S6                      | Switch     | Siemens Scalance XB008                                        | N/A (unmanaged) | N/A (unmanaged)   | Ethernet                       | Station 6 network distribution |
| PLC S6                         | PLC        | Siemens CPU 1512SP F-1 PN (S7-1500, ET 200SP series) / V3.0.3 | 172.21.6.1      | 30:B8:51:32:D4:5F | PROFINET, HTTP, OPC-UA, S7comm | Process control S6             |
| Power Monitor S6               | Monitor    | ?                                                             | 172.21.6.61     | 10:DF:FC:17:DC:6C | ?                              | Power consumption monitoring   |
| CPX Programmable Controller S6 | Controller | Festo                                                         | 172.21.6.60     | 00:0E:F0:93:AF:99 | PROFINET                       | ?                              |

### Switch S6 – Port Connections

| Port | Connected To  |
|------|---------------|
| P1   | Switch S5     |
| P2   | Power Monitor |
| P3   | PLC S6        |
| P4   | —             |
| P5   | —             |
| P6   | —             |
| P7   | —             |
| P8   | —             |

---
