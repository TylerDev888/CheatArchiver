# Daytona USA

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00630  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set range:0x000010,0x000557)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
