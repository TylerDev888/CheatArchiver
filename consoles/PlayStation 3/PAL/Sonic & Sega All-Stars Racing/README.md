# Sonic & Sega All-Stars Racing

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00750  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For Profile.dat (required)
**Author:**   
**Notes:** File: PROFILE.DAT  (set [csum]:dwadd(0x000004,0x0A5FFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000004,pointer)
write at 0x000000:[csum]
```

---
