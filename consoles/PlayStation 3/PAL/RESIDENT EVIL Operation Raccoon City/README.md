# RESIDENT EVIL Operation Raccoon City

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01288  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Xp
**Author:**   
**Notes:** File: RERC.DAT

```
search B848511000000000
write next 8:05F5E0FF
```

---

### Level 99(win 1 More Xp To Be Level 99)
**Author:**   
**Notes:** File: RERC.DAT

```
search 0x650BFF80
write next (-4):0x60000000
```

---

### Max Xp(alt)
**Author:**   
**Notes:** File: RERC.DAT

```
80010004 B8485110
28000008 05F5E0FF
```

---

### Update Crc32 For Rerc.dat (required)(by Chaoszage)
**Author:**   
**Notes:** File: RERC.DAT  (set range:0x000004,0x063FFF)

```
set [start]:read(0x50,4)
set [add]:read(0x54,4)
set [end]:[start]+[add]-1
set range:[start],[end]
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000058:[hash]
set [hash]:0
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
