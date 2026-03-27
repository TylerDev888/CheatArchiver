# F1 2011

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01311  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For Savedata (required)
**Author:**   
**Notes:** File: SAVEDATA  (set [csum]:dwadd(0xC,0x07FFFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0xC,pointer)
write at 0x000000:[csum]
```

---
