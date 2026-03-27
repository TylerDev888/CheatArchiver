# Karaoke Revolution Presents_ American Idol Encore

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30112  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big:0 For Gamesave (required)
**Author:**   
**Notes:** File: GAMESAVE  (set range:0x00000C,0x025FCB)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000008:[hash]
```

---
