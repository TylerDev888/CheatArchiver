# Vancouver 2010 - The Official Video Game of the Olympic Winter Games

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00660  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Save.bin (required)
**Author:**   
**Notes:** File: SAVE.BIN  (set range:0x10,0x000407)

```
set pointer:eof+1
set range:0x10,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
