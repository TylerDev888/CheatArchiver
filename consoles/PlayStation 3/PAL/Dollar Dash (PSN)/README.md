# Dollar Dash (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01058  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: PAYLOAD

```
write at 0x00000113:0x98967F00
```

---

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x0000CA)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
