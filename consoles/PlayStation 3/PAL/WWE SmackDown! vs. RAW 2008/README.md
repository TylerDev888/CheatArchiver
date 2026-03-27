# WWE SmackDown! vs. RAW 2008

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00137  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Save.dat (required)
**Author:**   
**Notes:** File: SAVE.DAT  (set [csum]:add(0x20,0x508B27))

```
set [csum]:0
set pointer:eof-8
set [csum]:add(0x20,pointer)
write at 0x000018:[csum]
```

---
