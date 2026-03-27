# LEGO The Hobbit

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01998  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Update Checksum For Game1 (required)
**Author:**   
**Notes:** File: GAME1

```
set pointer:eof+1
set range:0x14,pointer
set [hash]:fnv1:0xFFFFFFFF
set [hash]:xor:FFFFFFFF
write at 0x0010:[hash]
```

---
