# ICS Risk Assessment

## Risk Matrix Table

| Threat                                           | Likelihood | Impact (Safety / Production / Education)                                          | Risk Score | Priority |
| ------------------------------------------------ | ---------- | --------------------------------------------------------------------------------- | ---------- | -------- |
| PLC logic manipulation                           | Medium (2) | Critical (4): unsafe actuator behaviour, production shutdown, learning disruption | 8          | High     |
| PLC command spoofing                             | Low (1)    | High (3): incorrect control actions, potential physical instability               | 3          | Low      |
| SCADA/HMI denial of service                      | Medium (2) | High (3): loss of operator visibility, production interruption                    | 6          | Medium   |
| Session hijacking (SCADA)                        | Low (1)    | High (3): stealth control manipulation, loss of trust in system                   | 3          | Low      |
| Engineering PC malware infection                 | High (3)   | Critical (4): full compromise of control layer, persistent attacker access        | 12         | Critical |
| Unauthorized engineering access (insider misuse) | Medium (2) | Critical (4): silent logic changes, safety bypass possible                        | 8          | High     |
| Rogue device in network                          | Medium (2) | Medium (2): reconnaissance, lateral movement                                      | 4          | Medium   |
| Network flooding / traffic storm                 | Medium (2) | High (3): loss of PLC communication, system downtime                              | 6          | Medium   |
| MES production manipulation                      | Medium (2) | High (3): incorrect production runs, financial + operational impact               | 6          | Medium   |
| Webshop/API data manipulation                    | Medium (2) | Medium (2): incorrect orders, indirect production issues                          | 4          | Medium   |
| PLC configuration/data exfiltration              | Medium (2) | High (3): loss of intellectual property + enables future attacks                  | 6          | Medium   |

---

