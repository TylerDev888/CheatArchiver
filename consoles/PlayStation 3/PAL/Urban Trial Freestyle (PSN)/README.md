# Urban Trial Freestyle (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01238  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Cash
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0x000002A3:0x1869F069
```

---

### Update Dwadd For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set [csum]:dwadd(0x000078,0x0E7FFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000078,pointer)
write at 0x000034:[csum]
```

---
