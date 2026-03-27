# Resistance 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES00226  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Game.sav (required)
**Author:**   
**Notes:** File: GAME.SAV  (set range:0x20,0x060277)

```
set pointer:EOF-7
set range:0x20,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x00000C:[hash]
```

---
