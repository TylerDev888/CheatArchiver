# Turok

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00187  
**Cheat Type:** Save Editor  

---

## Cheats

### Get Crc32big:0 For Userdata (required)
**Author:**   
**Notes:** File: USERDATA

```
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
```

---

### Update Crc32big:0 For Header (required)
**Author:**   
**Notes:** File: HEADER

```
write at 0x000008:[hash]
set [hash]:0
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---
