# SEGA Vintage Collection_ Sonic The Hedgehog 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00477  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x0B8479)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
