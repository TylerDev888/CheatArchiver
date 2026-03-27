# BlazBlue_ Chronophantasma Extend

**Console:** PlayStation Vita  
**Region:** PAL  
**Serial:** PCSB00863  
**Cheat Type:** Save Editor  
**Source:** [Credits: Bucanero](Credits: Bucanero)  

---

## Cheats

### 9999999 P$
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
20007F50 0098967F
```

---

### Unlock All Gallery
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
420001A0 02020202
40B00004 00000000
```

---

### Update Wadd For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT  \\\\carry(2)

```
set [csum]:0
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
