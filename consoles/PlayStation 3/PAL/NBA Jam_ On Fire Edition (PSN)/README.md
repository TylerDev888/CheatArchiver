# NBA Jam_ On Fire Edition (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00650  
**Cheat Type:** AP  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x00001C,0x03D0AB)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
