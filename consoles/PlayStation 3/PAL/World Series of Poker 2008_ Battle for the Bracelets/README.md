# World Series of Poker 2008_ Battle for the Bracelets

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00139  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savefile.sav (required)
**Author:**   
**Notes:** File: SAVEFILE.SAV  (set range:0x000008,0x030FFF)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
