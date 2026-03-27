# Cartoon Network_ Punch Time Explosion XL

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01622  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie PS3](From Game Genie PS3)  

---

## Cheats

### Max Points
**Author:**   
**Notes:** File: GDATA

```
2000001C 47C35000
```

---

### Update Crc32 For Game (required)
**Author:**   
**Notes:** File: GAME  (set range:0x000024,0x001043)

```
set pointer:eof+1
set range:0x000024,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
