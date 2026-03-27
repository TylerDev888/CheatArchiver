# R.I.P.D. Rest In Peace Department - The Game

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31221  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Gold(by Fileover)
**Author:**   
**Notes:** File: SAVES.CFG

```
20000109 0098967F
2000010D 0098967F
```

---

### Update Crc32 For Saves.cfg (required)(checksum By Aldostoos)
**Author:**   
**Notes:** File: SAVES.CFG

```
set range:0x24,0xF8
set [hash]:CRC32
write at 0x000020:[hash]
set [hash]:00000000
set range:0x0000FD,0x190
set [hash]:CRC32
write at 0x0000F9:[hash]
```

---
