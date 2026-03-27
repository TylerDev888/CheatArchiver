# Call of Duty 4_ Modern Warfare

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00149  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savegame.svg (required)
**Author:**   
**Notes:** File: SAVEGAME.SVG  (set range:0x454,0x02AE6D)

```
set pointer:eof+1
set range:0x454,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
