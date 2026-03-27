# Contrast (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01861  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000024,0x00C3FB)

```
set pointer:eof+1
set range:0x000024,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
