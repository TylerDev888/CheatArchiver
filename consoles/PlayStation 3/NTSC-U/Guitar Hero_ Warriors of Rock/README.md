# Guitar Hero_ Warriors of Rock

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30487  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Toc.dat (required)
**Author:**   
**Notes:** File: TOC.DAT  (set range:0x000004,0x00753F)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
