# Hasbro Family Game Night 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00973  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd (required)
**Author:**   
**Notes:** File: PROFILE.DAT  (set [csum]:dwadd(0x000004,0x0007FF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000004,pointer)
write at 0x000000:[csum]
```

---
