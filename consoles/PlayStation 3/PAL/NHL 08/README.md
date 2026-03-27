# NHL 08

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00118  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x1C,0x12E5CF)

```
set pointer:eof+1
set range:0x1C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
