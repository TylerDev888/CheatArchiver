# Blazblue_ Continuum Shift EXTEND

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM60394  
**Cheat Type:** AP  
**Source:** [aldotools](aldotools)  

---

## Cheats

### Update Wadd For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set [csum]:wadd(0x000004,0x0E89E7))

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
