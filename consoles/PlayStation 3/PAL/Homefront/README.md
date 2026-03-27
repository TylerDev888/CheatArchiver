# Homefront

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00962  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x0004EE)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32Big
write at 0x000000:[hash]
```

---
