# Pro Evolution Soccer 2012

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01406  
**Cheat Type:** AP  
**Source:** [From aldotools](From aldotools)  

---

## Cheats

### Update Crc32 For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x0,0x04C51F)

```
write at 0x000008:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
