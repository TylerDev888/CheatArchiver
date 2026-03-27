# Need for Speed™ Undercover

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00450  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (cheats should go here)

```
set pointer:read(0x64, 4)
set range:0x000070,pointer+0x5B
DECRYPT nfs_undercover
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set pointer:read(0x64, 4)
set range:0x000070,pointer+0x5B
ENCRYPT nfs_undercover
```

---
