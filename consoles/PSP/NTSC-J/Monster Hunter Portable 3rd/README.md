# Monster Hunter Portable 3rd

**Console:** PSP  
**Region:** NTSC-J  
**Serial:** ULJM05800  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Decrypt Mhp3rd.bin (required)
**Author:**   
**Notes:** File: MHP3RD.BIN

```
set range:0x0000,EOF+1
DECRYPT monster_hunter(3)
```

---

### Update Custom Sha1 (required)
**Author:**   
**Notes:** File: MHP3RD.BIN

```
add salt at (size-36), then calc sha1)
hash stored at (size-24))
set pointer:EOF-0x23
set [temp]:read(pointer, 0x14)
write next (0):\
set range:0x0000,EOF-0x10
set [shasum]:SHA1
write next (0):[temp]
write next (12):[shasum]
```

---

### Encrypt Mhp3rd.bin (required)
**Author:**   
**Notes:** File: MHP3RD.BIN

```
set range:0x0000,EOF+1
ENCRYPT monster_hunter(3)
```

---
