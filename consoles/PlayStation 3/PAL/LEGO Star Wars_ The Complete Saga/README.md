# LEGO Star Wars_ The Complete Saga

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00121  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For Savedata.dat(required)
**Author:**   
**Notes:** File: SAVEDATA.DAT  (set [csum]:dwadd(0x000000,0x007E4B)) (write at 0x0x007E4C:[csum])

```
set pointer:EOF-4
set [csum]:0x5C0999
set [csum]:dwadd(0x000000,pointer)
set pointer:EOF-3
write next 0:[csum]
```

---
