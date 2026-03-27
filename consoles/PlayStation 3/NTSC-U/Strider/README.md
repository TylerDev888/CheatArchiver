# Strider

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31139  
**Cheat Type:** AP  

---

## Cheats

### Update Crc32 For Savegame (required)(checksum Found By Chaoszage)
**Author:**   
**Notes:** File: SAVEGAME  (set range:0x007804,0x0FFFFF)

```
set range:0x000004,0x077FF
set [hash]:CRC32
write at 0x000000:[hash]
set [hash]:0
set pointer:eof+1
set range:0x007804,pointer
set [hash]:CRC32
write at 0x007800:[hash]
```

---
