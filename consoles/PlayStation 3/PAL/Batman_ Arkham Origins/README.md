# Batman_ Arkham Origins

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01784  
**Cheat Type:** AP  

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
**Notes:** File: SPBATMAN  (set range:0x000000,0x047FFB) (write at 0x047FFC:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big
set pointer:eof-3
write next (0):[hash]
```

---
