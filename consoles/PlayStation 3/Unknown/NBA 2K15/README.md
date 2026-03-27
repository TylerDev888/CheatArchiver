# NBA 2K15

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10287  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Userdata (required)
**Author:**   
**Notes:** File: USERDATA  (set range:0x000004,0x7E8C1E)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
