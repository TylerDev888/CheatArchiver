# TimeShift

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00159  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Save.tss (required)
**Author:**   
**Notes:** File: SAVE.TSS  (set range:0x000004,0x0C97FF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
