# Age of Booty

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00035  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Gamedata (required)
**Author:**   
**Notes:** File: GAMEDATA  (set range:0x000008,0x00002F)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
