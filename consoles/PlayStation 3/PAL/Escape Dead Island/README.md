# Escape Dead Island

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02026  
**Cheat Type:** Save Editor  
**Source:** [from shaka](from shaka)  

---

## Cheats

### Update Crc32 For Save.sav (required)
**Author:**   
**Notes:** File: SAVE.SAV  (set range:0x000004,0x004C21)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
