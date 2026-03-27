# Saints Row 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00373  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: BLES00373*\\SYS-DATA

```
200000B8 3B9AC9FF
```

---

### Update Crc32:0 For Sys-data (required)
**Author:**   
**Notes:** File: BLES00373*\\SYS-DATA  (set range:0x000004,0x03ABFF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32:0
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
