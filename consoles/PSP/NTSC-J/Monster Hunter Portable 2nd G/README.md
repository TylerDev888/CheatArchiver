# Monster Hunter Portable 2nd G

**Console:** PSP  
**Region:** NTSC-J  
**Serial:** ULJM05500  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Decrypt Mhp2ndg.bin (required)
**Author:**   
**Notes:** File: MHP2NDG.BIN

```
set range:0x0000,EOF+1
DECRYPT monster_hunter(2)
```

---

### Unlock Bonus Content
**Author:**   
**Notes:** File: MHP2NDG.BIN

```
20000020 07FFFBFF
```

---

### Quest MOD
**Author:**   
**Notes:** File: MHP2NDG.BIN

```
95000000 [XXXXXXXX]
[QUEST1]
[QUEST2]
```

---

### Update Custom Sha1 (required)
**Author:**   
**Notes:** File: MHP2NDG.BIN

```
add salt at (size-36), then calc sha1
hash stored at (size-24)
set pointer:EOF-0x23
set [temp]:read(pointer, 0x14)
write next (0):\
set range:0x0000,EOF-0x10
set [shasum]:SHA1
write next (0):[temp]
write next (12):[shasum]
```

---

### Encrypt Mhp2ndg.bin (required)
**Author:**   
**Notes:** File: MHP2NDG.BIN

```
set range:0x0000,EOF+1
ENCRYPT monster_hunter(2)
```

---
