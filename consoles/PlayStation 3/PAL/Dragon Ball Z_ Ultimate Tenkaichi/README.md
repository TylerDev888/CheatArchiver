# Dragon Ball Z_ Ultimate Tenkaichi

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01401  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Update Checksum For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA

```
set pointer:eof+1
set [csum]:0
set [csum]:wadd_le(0x0008,pointer)
write at 0x0004:[csum]
write at 0x0001:[csum]
write at 0x0004:0x000000
```

---
