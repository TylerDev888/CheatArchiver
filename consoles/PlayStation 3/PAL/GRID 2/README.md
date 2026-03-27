# GRID 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01737  
**Cheat Type:** Save Editor  

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

### Update Sha256 For Progress.dat (required)
**Author:**   
**Notes:** File: PROGRESS.DAT  (set range:0x000000,0x002F9B)

```
set pointer:lastbyte-0x1F
set range:0x000000,pointer
set [hash]:SHA256
write next (0):[hash]
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
