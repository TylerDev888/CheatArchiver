# Shantae and the Pirate's Curse

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA01609  
**Cheat Type:** AP  
**Source:** [checksum by Zhaxxy](checksum by Zhaxxy)  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: *  \\\\Decompress(*, -15)

---

### Compress Save (required)
**Author:**   
**Notes:** File: *  \\\\Compress(*)

---

### Update Jhash (required)
**Author:**   
**Notes:** File: *

```
set range:0x0004,EOF+1
set [csum]:jhash
set [csum]:[csum]+0x4900DC7C
set [csum]:endian_swap
write at 0x0000:[csum]
```

---
