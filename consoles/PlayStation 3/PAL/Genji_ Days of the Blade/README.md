# Genji_ Days of the Blade

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES00002  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (set [csum]:add(0x000010,0x00FFFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000010,pointer)
write at 0x00000C:[csum]
```

---
