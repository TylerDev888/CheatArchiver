# MySims SkyHeroes

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01088  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 (required)
**Author:**   
**Notes:** File: MSF  (set range:0x00000C,0x005EF7)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
