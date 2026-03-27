# The Orange Box

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00153  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Calculate Crc32 For .cfg
**Author:**   
**Notes:** File: *.CFG

```
set range:0x00,eof+1
set [hash]:crc32
```

---

### Write New Crc32 To .chk
**Author:**   
**Notes:** File: *.CHK

```
write at 0x00:[hash]
```

---
