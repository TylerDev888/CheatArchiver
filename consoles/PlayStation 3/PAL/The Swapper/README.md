# The Swapper

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01940  
**Cheat Type:** Save Editor  
**Source:** [from aldotools](from aldotools)  

---

## Cheats

### Update Crc32big:0 For Data_0.bin (required)
**Author:**   
**Notes:** File: DATA_0.BIN  (set range:0x000000,0x00002F) (write at 0x000030:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---
