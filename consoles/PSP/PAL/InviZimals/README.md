# InviZimals

**Console:** PSP  
**Region:** PAL  
**Serial:** UCES01241  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Update Custom Adler32 (required)
**Author:**   
**Notes:** File: GAMEDATA

```
write at 0x000C:0x99674588
set range:0x0000,EOF+1
set [hash]:Adler32:0x00000000
set [hash]:endian_swap
write at 0x000C:[hash]
```

---
