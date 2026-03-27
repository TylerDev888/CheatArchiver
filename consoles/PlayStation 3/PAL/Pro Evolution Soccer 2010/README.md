# Pro Evolution Soccer 2010

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00689  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x000000,0x44DEF7)

```
write at 0x000008:00000000
set pointer:eof+1
set range:0x000000,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
