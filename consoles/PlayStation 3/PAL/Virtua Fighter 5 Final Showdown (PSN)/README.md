# Virtua Fighter 5 Final Showdown (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00913  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set range:0x000010,0x00500B)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
