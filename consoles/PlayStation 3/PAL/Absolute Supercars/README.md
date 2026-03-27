# Absolute Supercars

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01500  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add (required)
**Author:**   
**Notes:** File: SYS-DATA

```
set [csum]:0
set [csum]:add(0x00000C,0x112703)
set pointer:eof+1
set [csum]:add(0x00000C,pointer)
write at 0x000008:[csum]
```

---
