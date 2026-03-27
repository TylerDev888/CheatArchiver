# Street Fighter IV

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00481  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Sf4-save.dat (required)
**Author:**   
**Notes:** File: SF4-SAVE.DAT  (set range:0x000004,0x004BCE)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Sf4svext.dat (required)
**Author:**   
**Notes:** File: SF4SVEXT.DAT  (set range:0x000004,0x003F83)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
