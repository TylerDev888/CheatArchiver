# Dead To Rights_ Retribution

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00824  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Unlock All Chapters & Extras
**Author:**   
**Notes:** File: GAMESAVE

```
42000150 00000001
400B0004 00000000
```

---

### Update Crc32big:0 (required)
**Author:**   
**Notes:** File: GAMESAVE  (set range:0x000010,0x04900F)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000008:[hash]
```

---
