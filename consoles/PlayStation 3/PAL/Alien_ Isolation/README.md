# Alien_ Isolation

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01697  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Update Sha1 Xor64 For Sthefile (required)
**Author:**   
**Notes:** File: STHEFILE

```
set [off1]:read(0x18, 4)
set [off2]:read(0x1C, 4)
set pointer:[off1]+[off2]-1
set range:0x20,pointer
set [csum]:sha1_xor64
write at 0x08:[csum]
```

---

### Update Sha1 Xor64 For Othefile (required)
**Author:**   
**Notes:** File: OTHEFILE

```
set [off1]:read(0x18, 4)
set [off2]:read(0x1C, 4)
set pointer:[off1]+[off2]-1
set range:0x20,pointer
set [csum]:sha1_xor64
write at 0x08:[csum]
```

---
