# TRANSFORMERS_ Revenge of the Fallen

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00577  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savegame.dat (required)
**Author:**   
**Notes:** File: SAVEGAME.DAT  (set range:0x000008,0x002037)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
