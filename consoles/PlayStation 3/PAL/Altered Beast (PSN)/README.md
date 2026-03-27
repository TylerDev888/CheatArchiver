# Altered Beast (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00526  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x0C668F)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
