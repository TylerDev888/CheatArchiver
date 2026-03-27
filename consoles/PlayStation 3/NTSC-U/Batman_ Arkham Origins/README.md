# Batman_ Arkham Origins

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31147  
**Cheat Type:** AP  
**Source:** [From zeick](From zeick)  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: SPBATMAN

```
Decompress(*, 15)
```

---

### 9000000 Xp
**Author:**   
**Notes:** File: ~extracted\\*.dat

```
search \
write next (73):0x00895440
```

---

### 99 Upgrade Points
**Author:**   
**Notes:** File: ~extracted\\*.dat

```
search \
write next (32):0x63
```

---

### Compress Save (required)
**Author:**   
**Notes:** File: SPBATMAN

```
Compress(*)
```

---

### Update Crc32big For Spbatman (required)
**Author:**   
**Notes:** File: SPBATMAN  (write at 0x047FFC:[hash])

```
set range:0x000000,0x047FFB
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big
set pointer:eof-3
write next (0):[hash]
```

---

### Update Sha1 For Mpsave (required)
**Author:**   
**Notes:** File: MPSAVE

```
set range:0x000014,0x00074E
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
