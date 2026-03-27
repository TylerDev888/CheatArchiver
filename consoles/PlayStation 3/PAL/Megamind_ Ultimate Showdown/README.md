# Megamind_ Ultimate Showdown

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00867  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x000000,0x00508B) (write at 0x00508C:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next (0):[hash]
```

---
