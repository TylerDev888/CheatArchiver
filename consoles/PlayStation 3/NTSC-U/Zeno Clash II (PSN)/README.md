# Zeno Clash II (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30872  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x00045D)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
