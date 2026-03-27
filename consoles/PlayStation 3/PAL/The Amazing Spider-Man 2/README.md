# The Amazing Spider-Man 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01989  
**Cheat Type:** Save Editor  

---

## Cheats

### Tech Upgrades (999999)
**Author:**   
**Notes:** File: GAMEDATA

```
200057BC 000F423F
```

---

### Update Crc32 For Gamedata (required)
**Author:**   
**Notes:** File: GAMEDATA  (set range:0x000004,0x024EA3)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
