# SAMURAI WARRIORS 4

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31564  
**Cheat Type:** Save Editor  
**Source:** [from JP version,original cheats from savedata.jp](from JP version,original cheats from savedata.jp)  

---

## Cheats

### Max Gold
**Author:**   
**Notes:** File: DATA.BIN

```
20007842 000F423F
```

---

### Max Kills
**Author:**   
**Notes:** File: DATA.BIN

```
2000784A 05F5E0FF
```

---

### All Gems Max
**Author:**   
**Notes:** File: DATA.BIN

```
200078BC 63636363
200078C0 63636363
```

---

### All Chars Proficiency Max
**Author:**   
**Notes:** File: DATA.BIN

```
42000C44 14141414
403C0044 00000000
```

---

### All 1st Weapon Become Rare
**Author:**   
**Notes:** File: DATA.BIN

```
40003883 00000000
403C0110 00000002
```

---

### All 1st Weapon Skills Mod
**Author:**   
**Notes:** File: DATA.BIN

```
42003884 05050505
403C0110 00000000
42003888 05050505
403C0110 00000000
4200388C [SKILLS][SKILLS][SKILLS][SKILLS]
403C0110 00000000
42003890 [SKILLS][SKILLS][SKILLS][SKILLS]
403C0110 00000000
42003894 05050505
403C0110 00000000
42003898 05050505
403C0110 00000000
4200389C 02020202
403C0110 00000000
420038A0 02020202
403C0110 00000000
```

---

### All 1st Weapon Rare
**Author:**   
**Notes:** File: DATA.BIN

```
40003883 00000001
403C0110 00000002
```

---

### All 1st Weapon Become Rare And Skills Lv 5
**Author:**   
**Notes:** File: DATA.BIN

```
40003883 00000001
403C0110 00000002
42003884 05050505
403C0110 00000000
42003888 05050505
403C0110 00000000
4200388C [SKILLS][SKILLS][SKILLS][SKILLS]
403C0110 00000000
42003890 [SKILLS][SKILLS][SKILLS][SKILLS]
403C0110 00000000
42003894 05050505
403C0110 00000000
42003898 05050505
403C0110 00000000
4200389C 02020202
403C0110 00000000
420038A0 02020202
403C0110 00000000
```

---

### Exp 2,078,000 For Every Char
**Author:**   
**Notes:** File: DATA.BIN

```
42000C22 001FB530
40370044 00000000
```

---

### Musou Gauge X50
**Author:**   
**Notes:** File: DATA.BIN

```
40000C56 00000032
40370044 00000000
```

---

### Update Checksum For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN

```
write at 0x00004:0x00000000
write at 0x000A8:0x00000000
write at 0x00C16:0x00000000
write at 0x58532:0x00000000
set pointer:eof+1
set range:0x0000,pointer
set [hash]:sw4_checksum
set [crc1]:mid([hash],0x00,4)
set [crc2]:mid([hash],0x04,4)
set [crc3]:mid([hash],0x08,4)
set [crc4]:mid([hash],0x0C,4)
write at 0x00004:[crc1]
write at 0x000A8:[crc2]
write at 0x00C16:[crc3]
write at 0x58532:[crc4]
```

---
