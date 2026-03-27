# Cars Race-O-Rama

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30319  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For 0_data.dat (required)
**Author:**   
**Notes:** File: 0_DATA.DAT  (set [csum]:dwadd(0x000008,0x04DFFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000008,pointer)
write at 0x000000:[csum]
```

---
