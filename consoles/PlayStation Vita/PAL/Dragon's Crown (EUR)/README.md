# Dragon's Crown (EUR)

**Console:** PlayStation Vita  
**Region:** PAL  
**Serial:** PCSB00408  
**Cheat Type:** Save Editor  
**Source:** [Credits: Slade](Credits: Slade)  

---

## Cheats

### 9,999,999 Gold
**Author:**   
**Notes:** File: SAVE0.DAT

```
200AF288 0098967F
```

---

### 999 Skill Points
**Author:**   
**Notes:** File: SAVE0.DAT

```
1000A4F4 000003E7
```

---

### Level 255 (depends On Game Difficulty)
**Author:**   
**Notes:** File: SAVE0.DAT

```
0000A4F6 000000FF
```

---

### 999 Current Health
**Author:**   
**Notes:** File: SAVE0.DAT

```
1000A4DC 000003E7
```

---

### 999 Max Health
**Author:**   
**Notes:** File: SAVE0.DAT

```
1000A4E0 000003E7
```

---

### Update Crc32 For Save0.dat (required)
**Author:**   
**Notes:** File: SAVE0.DAT  (crc32 is stored in little-endian)

```
set pointer:eof+1
set range:0x04,pointer
set [crc]:crc32
set [crc]:endian_swap
write at 0x00:[crc]
```

---
