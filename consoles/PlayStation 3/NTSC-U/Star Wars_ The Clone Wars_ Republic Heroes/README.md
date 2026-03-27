# Star Wars_ The Clone Wars_ Republic Heroes

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30394  
**Cheat Type:** Save Editor  

---

## Cheats

### 9999 Points
**Author:**   
**Notes:** File: SAVE.DAT

```
20001F58 0000270F
```

---

### Update Crc32 For Save.dat (required)
**Author:**   
**Notes:** File: SAVE.DAT  (set range:0x000004,0x005003)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
