# Arcana Heart 3

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM60248  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Wadd For System.dat (required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set [csum]:wadd(0x000004,0x001187))

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
