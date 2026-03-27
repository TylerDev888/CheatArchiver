# Happy Feet Two_ The Videogame

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01425  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 (required)
**Author:**   
**Notes:** File: SAVE*.DAT  (set range:0x000008,0x000B9F)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
