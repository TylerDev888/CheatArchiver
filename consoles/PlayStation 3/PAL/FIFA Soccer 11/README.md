# FIFA Soccer 11

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01059  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x00001C,0x071132)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
