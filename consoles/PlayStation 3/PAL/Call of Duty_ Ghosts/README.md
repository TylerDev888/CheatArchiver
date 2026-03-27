# Call of Duty_ Ghosts

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01945  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Adler32 For Savegame.svg (required)
**Author:**   
**Notes:** File: SAVEGAME.SVG  (set range:0x000500,0x0B0677)

```
set pointer:eof+1
set range:0x000500,pointer
set [hash]:Adler32
write at 0x000008:[hash]
```

---
