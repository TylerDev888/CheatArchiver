# FIFA 16

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02161  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x00001C,0x035D28)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
