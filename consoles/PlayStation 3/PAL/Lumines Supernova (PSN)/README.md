# Lumines Supernova (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00066  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x000000,0x00EDEF) (write at 0x00EDF0:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next (0):[hash]
```

---
