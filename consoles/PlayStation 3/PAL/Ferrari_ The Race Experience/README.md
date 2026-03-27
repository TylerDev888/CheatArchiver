# Ferrari_ The Race Experience

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00185  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set [csum]:add(0x00000C,0x112703))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x00000C,pointer)
write at 0x000008:[csum]
```

---
