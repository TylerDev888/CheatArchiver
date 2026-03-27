# Quantum of Solace

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00406  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Savegame.svg (required)
**Author:**   
**Notes:** File: SAVEGAME.SVG  (set range:0x000454,0x08440E)

```
set pointer:eof+1
set range:0x000454,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
