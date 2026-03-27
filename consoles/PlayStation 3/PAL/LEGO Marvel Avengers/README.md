# LEGO Marvel Avengers

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02169  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Update Checksum For Game01 (required)
**Author:**   
**Notes:** File: GAME01

```
set [end]:read(0x14,4)
set range:0x18,[end]+0x17
set [hash]:fnv1:0xFFFFFFFF
set [hash]:xor:FFFFFFFF
write at 0x0010:[hash]
```

---
