# Virtua Tennis 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00027  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For System_l.dat (required)
**Author:**   
**Notes:** File: SYSTEM_L.DAT  (set [csum]:dwadd(0x000000,0x01CEEF)) (write at 0x01CEF0:[csum])

```
set [csum]:0
set pointer:eof-4
set [csum]:dwadd(0x000000,pointer)
set pointer:eof-3
write next (0):[csum]
```

---
