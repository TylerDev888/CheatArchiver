# LEGO Star Wars III_ The Clone Wars

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00934  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Update Checksum For Game1 (required)
**Author:**   
**Notes:** File: GAME1  (set pointer:eof-0xAE50) (set range:0x10,pointer)

```
set range:0x10,0xE1BF
set [hash]:fnv1:0xFFFFFFFF
set [hash]:xor:FFFFFFFF
write at 0x000C:[hash]
```

---
