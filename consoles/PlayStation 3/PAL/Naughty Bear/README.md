# Naughty Bear

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00945  
**Cheat Type:** Save Editor  
**Source:** [Fron aldotools](Fron aldotools)  

---

## Cheats

### Update Crc32 For Scores.dat (required)
**Author:**   
**Notes:** File: SCORES.DAT  (set range:0x00000C,0x0001C7)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Options.dat (required)
**Author:**   
**Notes:** File: OPTIONS.DAT  (set range:0x00000C,0x00001F)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
