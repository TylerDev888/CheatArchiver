# Monkey Island_ Special Edition Collection (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00191  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Gamedata (required)
**Author:**   
**Notes:** File: GAMEDATA  (set range:0x000008,0x00001F)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Monkey1.bin (required)
**Author:**   
**Notes:** File: MONKEY1.BIN  (set range:0x000008,0x089AD7)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
