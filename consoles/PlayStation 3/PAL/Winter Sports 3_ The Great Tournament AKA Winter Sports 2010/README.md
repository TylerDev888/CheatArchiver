# Winter Sports 3_ The Great Tournament AKA Winter Sports 2010

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00600  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savegame.dat(required)
**Author:**   
**Notes:** File: SAVEGAME.DAT  (set range:0x000004,0x00FBFF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
set [hash]:[hash]-1
write at 0x000000:[hash]
```

---
