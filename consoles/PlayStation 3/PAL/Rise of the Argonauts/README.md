# Rise of the Argonauts

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00418  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x0,0x011C52)

```
write at 0x000000:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32Big
write at 0x000000:[hash]
```

---
