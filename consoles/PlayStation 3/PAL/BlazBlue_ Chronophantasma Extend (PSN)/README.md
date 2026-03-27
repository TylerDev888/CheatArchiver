# BlazBlue_ Chronophantasma Extend (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB02351  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### 999999p$
**Author:**   
**Notes:** File: SYSTEM.DAT

```
20007F70 000F423F
```

---

### Unlock All Gallery
**Author:**   
**Notes:** File: SYSTEM.DAT

```
420001A0 02020202
40B00004 00000000
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
