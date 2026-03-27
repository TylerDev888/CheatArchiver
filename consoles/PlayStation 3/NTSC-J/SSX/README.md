# SSX

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLAS50445  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Credits
**Author:**   
**Notes:** File: BLAS5044500*\\SYS-DATA

```
80010008 20737949
76000000 20000000
28000009 BB9AC9FF
```

---

### Update Crc32big For Sys-data (required)
**Author:**   
**Notes:** File: BLAS5044500*\\SYS-DATA  (set range:0x000020,0x05781B)

```
set pointer:eof+1
set range:0x000020,pointer
set [hash]:CRC32Big
write at 0x00001C:[hash]
```

---
