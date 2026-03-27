# Geometry Wars 3_ Dimensions

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31544  
**Cheat Type:** Save Editor  
**Source:** [from aldostools](from aldostools)  

---

## Cheats

### Update Crc32 For Sav-data (required)
**Author:**   
**Notes:** File: SAV-DATA  (set range:0x000004,0x00B3FF)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
