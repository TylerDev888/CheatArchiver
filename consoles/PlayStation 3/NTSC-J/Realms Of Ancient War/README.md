# Realms Of Ancient War

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** NPJB00351  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Data.dat (required)
**Author:**   
**Notes:** File: NPJB00351-GAMESAVE*\\DATA.DAT

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: DATA.DAT

```
set range:0x000000,0x006E27
set pointer:eof-7
set range:0x000000,pointer
set [hash]:CRC32
write at 0x006E28:[hash]
set pointer:eof-7
write next (0):[hash]
```

---
