# El Chavo Kart

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31489  
**Cheat Type:** Save Editor  
**Source:** [by SHAkA](by SHAkA)  

---

## Cheats

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x00029A) (compress -w 15)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
