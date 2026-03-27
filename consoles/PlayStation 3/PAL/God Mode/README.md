# God Mode

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01300  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Xp
**Author:**   
**Notes:** File: SAVES.CFG

```
20000102 05F5E0FF
```

---

### Max Money
**Author:**   
**Notes:** File: SAVES.CFG

```
20000106 05F5E0FF
2000010A 05F5E0FF
```

---

### Update Crc32 For Saves.cfg (required)(checksum By Chaoszage)
**Author:**   
**Notes:** File: SAVES.CFG

```
set range:0x00000C,0x00001F
set [hash]:CRC32
write at 0x000008:[hash]
set [hash]:0
set range:0x000024,0x0000F5
set [hash]:CRC32
write at 0x000020:[hash]
set [hash]:0
set range:0x0000FA,0x26D
set [hash]:CRC32
write at 0x0000F6:[hash]
```

---
