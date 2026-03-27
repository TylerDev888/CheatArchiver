# Metal Gear Solid Peace Walker

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00686  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decrypt 00000000.000 (required)
**Author:**   
**Notes:** File: 00000000.000  (cheats should go here)

```
set range:0x0000,eof+1
DECRYPT mgs_pw
```

---

### Update Custom Checksums (required)
**Author:**   
**Notes:** File: 00000000.000  (checksum 1) (checksum 2) (checksum 3) (checksum 4)

```
set range:0x00044,0x1AF67
set [csum]:mgspw_checksum
write at 0x0038:[csum]
set range:0x1AF68,0x1CB67
set [csum]:mgspw_checksum
write at 0x003C:[csum]
set range:0x1CB68,0x359CF
set [csum]:mgspw_checksum
write at 0x0030:[csum]
set range:0x35A18,0x44AE7
set [csum]:mgspw_checksum
write at 0x35A0C:[csum]
```

---

### Encrypt 00000000.000 (required)
**Author:**   
**Notes:** File: 00000000.000

```
set range:0x0000,eof+1
ENCRYPT mgs_pw
```

---
