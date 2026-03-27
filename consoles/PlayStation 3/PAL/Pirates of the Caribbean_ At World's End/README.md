# Pirates of the Caribbean_ At World's End

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00066  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 (required)
**Author:**   
**Notes:** File: SAVE.DAT  (set range:0x000004,0x184F17)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
