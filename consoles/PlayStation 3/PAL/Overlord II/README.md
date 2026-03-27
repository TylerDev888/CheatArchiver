# Overlord II

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00580  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x000004,0x01A781)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
