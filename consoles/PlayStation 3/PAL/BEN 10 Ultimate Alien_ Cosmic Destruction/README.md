# BEN 10 Ultimate Alien_ Cosmic Destruction

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01110  
**Cheat Type:** Save Editor  

---

## Cheats

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

### Update Crc32 For Miss (required)
**Author:**   
**Notes:** File: MISS  (set range:0x24,0x00801F)

```
set pointer:eof+1
set range:0x24,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
