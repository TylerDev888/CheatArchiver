# Resistance_ Fall of Man

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES00001  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Profile.sav (required)
**Author:**   
**Notes:** File: PROFILE.SAV  (set range:0x000010,0x003387)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x00000C:[hash]
```

---
