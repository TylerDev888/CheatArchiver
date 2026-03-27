# Scourge_ Outbreak

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01220  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x000405)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
