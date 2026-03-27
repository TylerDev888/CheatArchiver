# DmC_ Devil May Cry

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01698  
**Cheat Type:** Save Editor  
**Source:** [By Dark Nacho](By Dark Nacho)  

---

## Cheats

### Decrypt Profile (required)
**Author:**   
**Notes:** File: PROFILE  (:BLUS30723_DLC_1*\\PROFILE)

```
set range:0x000000,eof+1
DECRYPT blowfish_ecb(\
```

---

### Infinite Health
**Author:**   
**Notes:** File: PROFILE

```
search 0x4D41584845414C54485F504C41594552
write next (16):0x00164E6E6B28
search 0x4D41584845414C54485F534554
write next (13):0x000000000001
```

---

### Infinite Devil Trigger
**Author:**   
**Notes:** File: PROFILE

```
search 0x4D415854524947474552504F494E54535F504C41594552
write next (23):0x00164E6E6B28
search 0x4D415854524947474552504F494E54535F534554
write next (20):0x000000000001
```

---

### Red Orb 999.999
**Author:**   
**Notes:** File: PROFILE

```
search 0x4F72625F526564
write next (7):0x0014000F423F
```

---

### Max Red Orbs
**Author:**   
**Notes:** File: PROFILE

```
80010008 4F72625F
52656400 00000000
28000009 000F423F
```

---

### Max Upgrade Points (not Working)
**Author:**   
**Notes:** File: PROFILE

```
62000000 0000152A
62100000 00001532
62400000 00000063
62100000 00000004
62400000 00000063
```

---

### Max Small Vital Stars
**Author:**   
**Notes:** [Standard Max]  File: PROFILE

```
8001000C 6C537461
725F536D 616C6C00
2800000D 0000000A
80010014 56697461
6C537461 725F536D
616C6C5F 50657273
2800001C 0000000A
```

---

### Max Large Vital Stars
**Author:**   
**Notes:** [Standard Max]  File: PROFILE

```
8001000C 6C537461
725F4C61 72676500
2800000D 0000000A
80010014 56697461
6C537461 725F4C61
7267655F 50657273
2800001C 0000000A
```

---

### Max Small Devil Trigger Star
**Author:**   
**Notes:** [Standard Max]  File: PROFILE

```
80010014 696C5472
69676765 72537461
725F536D 616C6C00
28000015 0000000A
8001001C 54726967
67657253 7461725F
536D616C 6C5F5065
72736973 74656E74
2800001E 0000000A
```

---

### Max Large Devil Trigger Star
**Author:**   
**Notes:** [Standard Max]  File: PROFILE

```
80010014 696C5472
69676765 72537461
725F4C61 72676500
28000015 0000000A
8001001C 54726967
67657253 7461725F
4C617267 655F5065
72736973 74656E74
2800001E 0000000A
```

---

### Max Gold Orbs
**Author:**   
**Notes:** [Standard Max]  File: PROFILE

```
80010008 72625F47
6F6C6400 00000000
28000009 00000003
80010013 4F72625F
476F6C64 5F506572
73697374 656E7400
28000015 00000003
```

---

### Dlc - Max Red Orbs
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
80010008 4F72625F
52656400 00000000
28000009 000F423F
```

---

### Dlc - Max Small Vital Stars
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
8001000C 6C537461
725F536D 616C6C00
2800000D 00000063
80010014 56697461
6C537461 725F536D
616C6C5F 50657273
2800001C 00000063
```

---

### Dlc - Max Large Vital Stars
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
8001000C 6C537461
725F4C61 72676500
2800000D 00000063
80010014 56697461
6C537461 725F4C61
7267655F 50657273
2800001C 00000063
```

---

### Dlc - Max Small Devil Trigger Star
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
80010014 696C5472
69676765 72537461
725F536D 616C6C00
28000015 00000063
8001001C 54726967
67657253 7461725F
536D616C 6C5F5065
72736973 74656E74
2800001E 00000063
```

---

### Dlc - Max Large Devil Trigger Star
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
80010014 696C5472
69676765 72537461
725F4C61 72676500
28000015 00000063
8001001C 54726967
67657253 7461725F
4C617267 655F5065
72736973 74656E74
2800001E 00000063
```

---

### Dlc - Max Gold Orbs
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
80010008 72625F47
6F6C6400 00000000
28000009 00000063
80010013 4F72625F
476F6C64 5F506572
73697374 656E7400
28000015 00000063
```

---

### Dlc - Infinite Health(don't Buy Health Upgrades)
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
80010010 4D415848
45414C54 485F504C
41594552 00000000
28000010 00164E6E
18000014 00006B28
28000029 00000001
```

---

### Dlc - Max Upgrade Points(from Eminem451)
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
62000000 00000888
62100000 00000890
62400000 00000063
62100000 00000004
62400000 00000063
```

---

### Dlc - Max Score(from Eminem451)
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
420001B8 00000006
40060021 00000000
400001BC 00000001
40060021 00000000
420001BD 05F5E0FF
40060021 00000000
```

---

### Dlc - Max Style(from Eminem451)
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
420001C1 00000006
40060021 00000000
420001C5 0098967F
40060021 00000000
```

---

### Dlc - 100% Completion(from Eminem451)
**Author:**   
**Notes:** [Virgil's Downfall Dlc]  File: PROFILE

```
420001D1 00000006
40060021 00000000
400001D8 00000064
40060021 00000000
```

---

### Update Sha1 For Profile (required)
**Author:**   
**Notes:** [Checksum]  File: PROFILE

```
set pointer:read(0x18, 4)
set range:0x00001C,pointer+0x1B
set [hash]:SHA1
write at 0x4:[hash]
```

---

### Encrypt Profile (required)
**Author:**   
**Notes:** [Checksum]  File: PROFILE

```
set range:0x000000,eof+1
ENCRYPT blowfish_ecb(\
```

---
