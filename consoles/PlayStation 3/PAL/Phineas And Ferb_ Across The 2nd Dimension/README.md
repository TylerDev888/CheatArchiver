# Phineas And Ferb_ Across The 2nd Dimension

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01349  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32:0 (required)
**Author:**   
**Notes:** File: SAVEGAME.BIN  (set range:0x000008,0x0040AF)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32:0
set [hash]:xor:FFFFFFFF
write at 0x000004:[hash]
```

---
