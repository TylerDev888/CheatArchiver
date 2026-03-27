# GRID Autosport

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02038  
**Cheat Type:** AP  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: PROGRESS.DAT

```
Decompress(*, -15)
```

---

### Compress Save (required)
**Author:**   
**Notes:** File: PROGRESS.DAT

```
Compress(*)
```

---

### Update Crc32 For Secuinfo.bin (required)
**Author:**   
**Notes:** File: SECUINFO.BIN  (set range:0x000004,0x000027)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Sha256 For Progress.dat (required)
**Author:**   
**Notes:** File: PROGRESS.DAT  (set range:0x000000,0x003EDE)

```
set pointer:eof-0x1F
set range:0x000000,pointer
set [hash]:sha256
write next (0):[hash]
```

---
