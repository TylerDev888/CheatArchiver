# Karaoke Revolution

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00694  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big:0 For Gamesave (required)
**Author:**   
**Notes:** File: GAMESAVE  (set range:0x000010,0x2D824F)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000008:[hash]
```

---
