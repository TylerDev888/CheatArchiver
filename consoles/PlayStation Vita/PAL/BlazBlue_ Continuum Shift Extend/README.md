# BlazBlue_ Continuum Shift Extend

**Console:** PlayStation Vita  
**Region:** PAL  
**Serial:** PCSB00042  
**Cheat Type:** Save Editor  
**Source:** [Credits: Bucanero](Credits: Bucanero)  

---

## Cheats

### 9999999 P$
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
200E3160 0098967F
```

---

### Unlock All Gallery
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
41000160 00000202
40F90002 00000000
```

---

### Player Level 33
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
200E3168 00017BCF
```

---

### Player Level 100
**Author:**   
**Notes:** File: SYSTEM/SYSTEM.DAT

```
200E3168 00FF423F
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
