# Legends of Wrestlemania

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00492  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Lgndsave.dat (required)
**Author:**   
**Notes:** File: LGNDSAVE.DAT  (set [csum]:add(0x20,0x49C64F))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x20,pointer)
write at 0x000018:[csum]
```

---
