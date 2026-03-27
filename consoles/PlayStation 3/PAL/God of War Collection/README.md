# God of War Collection

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES00791  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd (required)
**Author:**   
**Notes:** File: DATA*.BIN  (set [csum]:dwadd(0x000000,0x013FFB)) (write at 0x013FFC:[csum])

```
set [csum]:0
set pointer:eof-4
set [csum]:dwadd(0x000000,pointer)
set pointer:eof-3
write next (0):[csum]
```

---
