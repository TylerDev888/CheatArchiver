# Saints Row_ Gat out of Hell

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02095  
**Cheat Type:** Save Editor  
**Source:** [From gold972 and aldostools](From gold972 and aldostools)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0xFF90:0x3B9AC9FF
```

---

### Max Datacluster
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0xFF94:0x3B9AC9FF
```

---

### God Mod With Weapons
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0xFF48:0xBF800000
write at 0xFF4C:0xBF800000
write at 0xFF54:0xBF800000
write at 0xFF5C:0xBF800000
```

---

### Update Crc32:0 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x000004,0x025FFF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32:0
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
