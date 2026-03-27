# Metal Gear Solid 5_ The Phantom Pain

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA01140  
**Cheat Type:** AP  
**Source:** [encryption/checksum by bucanero](encryption/checksum by bucanero)  

---

## Cheats

### Decrypt Save Data (required)
**Author:**   
**Notes:** [CUSA01140]  File: TPP_GAME_DATA*

```
set range:0x0000,EOF+1
DECRYPT MGS5_TPP(0x4131F8BE)
```

---

### Update Md5 Checksum (required)
**Author:**   
**Notes:** [CUSA01140]  File: TPP_GAME_DATA*

```
set range:0x0010,EOF+1
set [hash]:MD5
write at 0x0000:[hash]
```

---

### Encrypt Save Data (required)
**Author:**   
**Notes:** [CUSA01140]  File: TPP_GAME_DATA*

```
set range:0x0000,EOF+1
ENCRYPT MGS5_TPP(0x4131F8BE)
```

---

### Max Heroism
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
2001C474 05F5E0FF
```

---

### Max Materials (processed)
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
42027138 000F4240
40050004 00000000
```

---

### Max Materials (unprocessed)
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
42027224 003D0900
40050004 00000000
```

---

### Max Medicinal Plant
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
4202714C 00002EE0
40080004 00000000
```

---

### Max Vehicle
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
4202716C 00061A80
400A0004 00000000
```

---

### Max Placed Weapon
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
420271C0 00061A80
40050004 00000000
```

---

### Max Walker Gear
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
42027194 00061A80
40050004 00000000
```

---

### Max Parasite
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
420271B0 00001770
40030004 00000000
```

---

### Infinite Clip Pistol Sniper And Assult Rifle
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
100047D6 0000FFFF
100047D8 0000FFFF
100047DA 0000FFFF
```

---

### Max Demon Points
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
2001C478 7FFFFFFF
```

---

### 0 Demon Points
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
2001C478 00000000
```

---

### 8 Nuclear Weapons
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
200271A8 00000010
```

---

### Max Resources (all)
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
42027138 000F4240
40050004 00000000
42027224 003D0902
40050004 00000000
4202714C 00002EE0
40080004 00000000
4202716C 00061A80
400A0004 00000000
420271C0 00061A80
40050004 00000000
42027194 00061A80
40050004 00000000
420271B0 00001770
40030004 00000000
200271AC 001E8480
```

---

### Build All Bases
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
4201C1D0 40014001
40110004 00000000
```

---

### Soldier Ranking System
**Author:**   
**Notes:** File: TPP_GAME_DATA*

```
4001FB34 0000004E
40[Amount:FF:HEX:BIG<soldiers>]0004 00000000
```

---
