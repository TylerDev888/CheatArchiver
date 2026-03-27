# Call of Duty_ Modern Warfare 2

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30377  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Adler32 For Savegame.svg (required)
**Author:**   
**Notes:** File: SAVEGAME.SVG  (set range:0x000480,0x06C277)

```
set pointer:eof+1
set range:0x000480,pointer
set [hash]:Adler32
write at 0x000008:[hash]
```

---
