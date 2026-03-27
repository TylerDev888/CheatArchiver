# Hatsune Miku_ Project Diva - Dreamy Theater (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** NPJB00047  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set range:0x10,0x050077)

```
set pointer:eof+1
set range:0x10,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
