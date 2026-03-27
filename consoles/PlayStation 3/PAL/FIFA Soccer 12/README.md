# FIFA Soccer 12

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01381  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)(uefa Euro 2012)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x00001C,0x079A4A)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
