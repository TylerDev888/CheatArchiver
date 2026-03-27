# de Blob 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01160  
**Cheat Type:** Save Editor  
**Source:** [From chaoszage](From chaoszage)  

---

## Cheats

### 999 Bulbs
**Author:**   
**Notes:** File: SAVEDATA

```
20000160 03E703E7
```

---

### All Stages Score 9999999
**Author:**   
**Notes:** File: SAVEDATA

```
420000D8 0098967F
400C0004 00000000
```

---

### Update Crc32:0 (required)(from Aldostools)
**Author:**   
**Notes:** File: SAVEDATA

```
write at 0x000008:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32:0
write at 0x000008:[hash]
```

---
