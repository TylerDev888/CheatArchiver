# Deadpool

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01789  
**Cheat Type:** Save Editor  
**Source:** [From zeick](From zeick)  

---

## Cheats

### Decompress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Decompress(0x00000018, 15)
```

---

### 999999 Dp Points
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
search 0x00004505
write next (4):497423F0
```

---

### Fix Compression (required)
**Author:**   
**Notes:** File: BLES01789-PROFILE\\PAYLOAD

```
delete at 0x20:0x4FF
```

---

### Compress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Compress(0x00000018)
```

---

### Update Sha1 (required)
**Author:**   
**Notes:** File: BLES01789-PROFILE\\PAYLOAD

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
