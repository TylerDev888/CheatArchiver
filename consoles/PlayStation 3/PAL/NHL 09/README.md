# NHL 09

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00298  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x1C,0x18015F)

```
set pointer:eof+1
set range:0x1C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
