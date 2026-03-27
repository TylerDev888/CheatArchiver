# BlazBlue_ Continuum Shift II

**Console:** PSP  
**Region:** Unknown  
**Serial:** NPJH50401  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Unlock All Gallery(by bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
41000160 00000101
40AD0002 00000000
```

---

### 9999999 P$ Credits
**Author:**   
**Notes:** File: SYSTEM.DAT

```
2002E378 0098967F
```

---

### Update Wadd For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
