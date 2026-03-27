# Trine 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00668  
**Cheat Type:** Save Editor  

---

## Cheats

### 99 Skill Points
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
write at 0x6A:0x63
```

---

### Update Md5 For Savedata.bin (required)
**Author:**   
**Notes:** File: SAVEDATA.BIN  (set range:0x0003E0,0x010535)

```
set pointer:eof+1
set range:0x0003E0,pointer
set [hash]:MD5
write at 0x0003D0:[hash]
```

---
