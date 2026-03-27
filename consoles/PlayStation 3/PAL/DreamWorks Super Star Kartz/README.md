# DreamWorks Super Star Kartz

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01373  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savegame.bin (required)
**Author:**   
**Notes:** File: SAVEGAME.BIN  (set range:0x000008,0x0011C7)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
