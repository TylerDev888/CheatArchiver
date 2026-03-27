# Blitz_ The League II

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00397  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big:0 For Bsav0.sav (required)
**Author:**   
**Notes:** File: BSAV0.SAV  (set range:0x000254,0x07C206)

```
set pointer:eof+1
set range:0x000254,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000250:[hash]
```

---
