# Orc Attack_ Flatulent Rebellion (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30614  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Skills Points
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0x0000005E:0xF0720063
```

---

### Max Money
**Author:**   
**Notes:** File: SYS-DATA

```
write at 0x0000003D:0xFB722860
```

---

### Update Md5 For Sys-data (required)
**Author:**   
**Notes:** File: SYS-DATA  (set range:0x000019,0x000256)

```
set pointer:eof+1
set range:0x000019,pointer
set [hash]:MD5
write at 0x000009:[hash]
```

---
