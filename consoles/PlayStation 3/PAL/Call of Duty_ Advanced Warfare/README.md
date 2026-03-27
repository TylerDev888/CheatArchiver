# Call of Duty_ Advanced Warfare

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02077  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Adler32 For Savegame.svg (required)
**Author:**   
**Notes:** File: SAVEGAME.SVG  (set range:0x500,0x0B94FA)

```
set pointer:eof+1
set range:0x500,pointer
set [hash]:Adler32
write at 0x000008:[hash]
```

---
