# Virtua Fighter 5

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00029  
**Cheat Type:** AP  

---

## Cheats

### Update Crc32 For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set range:0x000010,0x07B793)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
