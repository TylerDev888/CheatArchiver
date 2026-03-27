# BlazBlue_ Calamity Trigger

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00820  
**Cheat Type:** Save Editor  

---

## Cheats

### Unlock All Gallery(by Bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
41000160 00000101
40510002 00000000
```

---

### Update Wadd For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set [csum]:wadd(0x000004,0x0CFD5F))

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
