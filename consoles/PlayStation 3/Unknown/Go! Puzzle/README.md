# Go! Puzzle

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** NPEA00006  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32:0 For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
write at 0x4:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32:0
set [hash]:xor:FFFFFFFF
write at 0x4:[hash]
```

---
