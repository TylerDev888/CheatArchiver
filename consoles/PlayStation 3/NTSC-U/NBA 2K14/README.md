# NBA 2K14

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31204  
**Cheat Type:** AP  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Sp
**Author:**   
**Notes:** File: USERDATA

```
write at 0x007004E3:0x3B9AC9FF
```

---

### Update Crc32 For Userdata (required)
**Author:**   
**Notes:** File: USERDATA  (set range:0x000004,0x7B6C1D)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
