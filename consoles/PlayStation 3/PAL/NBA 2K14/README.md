# NBA 2K14

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01920  
**Cheat Type:** AP  

---

## Cheats

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
