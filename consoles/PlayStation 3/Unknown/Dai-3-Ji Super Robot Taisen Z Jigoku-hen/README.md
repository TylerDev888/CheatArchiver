# Dai-3-Ji Super Robot Taisen Z Jigoku-hen

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10256  
**Cheat Type:** Save Editor  

---

## Cheats

### Wadd Checksum Init (required)
**Author:**   
**Notes:** File: STAGE.BIN

```
set [value]:read(0x0, 2)
set [value]:endian_swap
set [csum]:0
set [csum]:wadd_le(0x00002,0x044060)
set [csum]:right([csum],2)
set [hash]:0
set [hash]:[value]-[csum]
```

---

### Max Funds 99,999,999
**Author:**   
**Notes:** File: STAGE.BIN

```
20000440 FFE0F505
```

---

### Stage Data Of All Characters Pp 65,535
**Author:**   
**Notes:** File: STAGE.BIN

```
4101E0C8 0000FFFF
41A500E0 00000000
```

---

### Stage Data Possession Z Chip 99,999
**Author:**   
**Notes:** File: STAGE.BIN

```
2000044C 9F860100
```

---

### Stage Total Data Acquisition Chip Z 99,999
**Author:**   
**Notes:** File: STAGE.BIN

```
20000450 9F860100
```

---

### 99 Pieces Stage All Data Enhancement Parts
**Author:**   
**Notes:** File: STAGE.BIN  (Please use Remove all if you are equipped with a reinforced parts.)

```
400005E8 00000063
40460018 00000000
400005EC 00000063
40460018 00000000
```

---

### All Data Stage Pilot Training All Max
**Author:**   
**Notes:** File: STAGE.BIN

```
4201E0E4 03030303
41A500E0 00000000
4201E0E8 90019001
41A500E0 00000000
4201E0EC 90019001
41A500E0 00000000
4201E0F0 90019001
41A500E0 00000000
```

---

### All Pilot Exp49000
**Author:**   
**Notes:** File: STAGE.BIN

```
4101E0F8 000068BF
41A500E0 00000000
```

---

### All Pilot Shot Down Number 999
**Author:**   
**Notes:** File: STAGE.BIN

```
4101E0FA 0000E703
41A500E0 00000000
```

---

### Stage Data Possession Funds 29,999,999
**Author:**   
**Notes:** File: STAGE.BIN

```
20000440 7FC3C901
```

---

### Stage Total Data Acquisition Funds 29,999,999
**Author:**   
**Notes:** File: STAGE.BIN

```
20000444 7FC3C901
```

---

### Main Character Skill Mod Love + Sniper + Assault + Air Force
**Author:**   
**Notes:** File: STAGE.BIN

```
20033D47 1D010100
20033D4B 0C010100
20033D4F 17010100
20033D53 19010100
20033D57 14010100
20033E27 1D010100
20033E2B 0C010100
20033E2F 17010100
20033E33 19010100
20033E37 14010100
20033FE7 1D010100
20033FEB 0C010100
20033FEF 17010100
20033FF3 19010100
20033FF7 14010100
```

---

### All Route Clear
**Author:**   
**Notes:** File: STAGE.BIN

```
42000044 FFFFFFFF
40080004 00000000
400000B8 000000FF
40330001 00000000
4000014A 000000FF
40120001 00000000
4000016A 000000FF
400E0001 00000000
4000018A 000000FF
40120001 00000000
```

---

### Wadd Checksum Update (required)
**Author:**   
**Notes:** File: STAGE.BIN

```
set [csum]:0
set [csum]:wadd_le(0x00002,0x044060)
set [csum]:right([csum],2)
set [hash]:[hash]+[csum]
set [hash]:right([hash],2)
set [hash]:endian_swap
write at 0x00:[hash]
```

---
