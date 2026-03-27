# NBA Street_ Homecourt

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00038  
**Cheat Type:** Save Editor  

---

## Cheats

### Get Eachecksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (set range:0x0,0x001DC7)

```
set pointer:eof+1
set range:0x0,pointer
set [hash]:EAChecksum
```

---

### Update Eachecksum In Hed-data (required)
**Author:**   
**Notes:** File: HED-DATA

```
write at 0x8:[hash]
```

---
