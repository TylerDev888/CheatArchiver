# Ferrari Challenge Trofeo Pirelli

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00166  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set [csum]:add(0x14,0x112703))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x14,pointer)
write at 0x000008:[csum]
```

---
