# BloodRayne Betrayal

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30377  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Adler32 For Save.dat (required)
**Author:**   
**Notes:** File: SAVE.DAT  (set range:0x000110,0x00040F)

```
set pointer:eof+1
set range:0x000110,pointer
set [hash]:Adler32
write at 0x000025:[hash]
```

---
