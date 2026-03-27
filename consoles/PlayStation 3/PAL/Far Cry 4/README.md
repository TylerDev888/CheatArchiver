# Far Cry 4

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02011  
**Cheat Type:** AP  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0x3C1E7604
write next 0x4:0xFFFFFF7F
```

---

### Max Skill Points By Dark Nacho
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0x3C1E7604
write next 0xF:0xF7
```

---

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
