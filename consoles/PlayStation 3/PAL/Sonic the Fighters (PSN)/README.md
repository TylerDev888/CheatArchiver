# Sonic the Fighters (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01162  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set range:0x000010,0x00107B)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
