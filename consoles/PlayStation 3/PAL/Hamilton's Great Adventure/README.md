# Hamilton's Great Adventure

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00169  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Autosave.sav (required)
**Author:**   
**Notes:** File: AUTOSAVE.SAV  (set range:0x000004,0x0002BF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
