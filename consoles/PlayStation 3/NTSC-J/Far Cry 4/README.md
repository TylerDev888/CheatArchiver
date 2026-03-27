# Far Cry 4

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM61179  
**Cheat Type:** AP  

---

## Cheats

### Update Crc32 & Md5 Hashes (required)
**Author:**   
**Notes:** File: SAVEDATA.000

```
set pointer:read(0xC,4)
set pointer:pointer+2F
set range:0x30, pointer
set [md5]:md5
write at 0x10:[md5]
set pointer:read(0xC,4)
set pointer:pointer+2F
set range:0x30, pointer
set [crc]:crc32
write at 0x20:[crc]
```

---
