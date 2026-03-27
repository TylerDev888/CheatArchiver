# Real Steel (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00754  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: SAVE.DAT

```
write at 0x00000098:0x3B9AC9FF
```

---

### Update Add For Save.dat (required)
**Author:**   
**Notes:** File: SAVE.DAT  (set [csum]:add(0x00001C,0x0084DF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x00001C,pointer)
write at 0x000018:[csum]
```

---
