# F1 2012

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01664  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Secuinfo.bin (required)
**Author:**   
**Notes:** File: SECUINFO.BIN

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
