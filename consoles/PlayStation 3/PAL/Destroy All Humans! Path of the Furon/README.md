# Destroy All Humans! Path of the Furon

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00467  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x004998) (write at 0x004999:[hash])

```
set pointer:eof-3
set range:0x000004,pointer
set [hash]:CRC32Big
set pointer:eof-3
write next (0):[hash]
```

---
