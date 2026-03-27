# NBA Jam_ On Fire Edition (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30558  
**Cheat Type:** AP  
**Source:** [From chaoszage](From chaoszage)  

---

## Cheats

### Max Coins
**Author:**   
**Notes:** File: SYS-DATA

```
search 0x7A68614B
write next 8:0x0098967F
```

---

### Max Coins 2
**Author:**   
**Notes:** File: SYS-DATA

```
20018DA8 0098967F
```

---

### Update Crc32 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x00001C,0x03D0AB)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:CRC32
write at 0x000010:[hash]
```

---
