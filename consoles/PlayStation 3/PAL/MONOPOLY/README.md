# MONOPOLY

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00387  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (set range:0x000008,0x001FFF)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
