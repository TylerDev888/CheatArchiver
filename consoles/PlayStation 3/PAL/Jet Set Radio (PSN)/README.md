# Jet Set Radio (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00924  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Qwadd (required)
**Author:**   
**Notes:** File: SLOT*.DAT  (set [csum]:qwadd(0x000000,0x04044B)) (write at 0x04044C:[csum])

```
set [csum]:0
set pointer:eof-4
set [csum]:qwadd(0x000000,pointer)
set pointer:eof-3
write next (0):[csum]
```

---
