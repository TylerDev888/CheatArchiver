# BlazBlue_ Calamity Trigger Portable

**Console:** PSP  
**Region:** Unknown  
**Serial:** NPJH50180  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Unlock All Gallery(by bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
41000160 00000101
40580002 00000000
00000210 00000001
```

---

### 9999999 Shop Credits
**Author:**   
**Notes:** File: SYSTEM.DAT

```
2002B80C 0098967F
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
