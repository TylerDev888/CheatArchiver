# THE INCREDIBLE HULK

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00289  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Hulk.sav (required)
**Author:**   
**Notes:** File: HULK.SAV  (set range:0xC,0x005E9F)

```
set pointer:eof+1
set range:0xC,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
