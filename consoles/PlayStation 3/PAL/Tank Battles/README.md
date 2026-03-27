# Tank Battles

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00158  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Xor For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (set [hash]:xor(0x000008,0x0003EF,4))

```
set [hash]:0
set pointer:eof+1
set [hash]:xor(0x000008,pointer,4)
write at 0x000010:[hash]
```

---
