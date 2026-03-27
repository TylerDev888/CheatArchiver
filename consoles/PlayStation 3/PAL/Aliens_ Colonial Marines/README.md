# Aliens_ Colonial Marines

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01455  
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

### Xenomorph 99 Upgrade Points
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000179:0x63
```

---

### Fix Compression
**Author:**   
**Notes:** File: BLES01455-PROFILE\\PAYLOAD

```
delete at 0x20:0x4FF
```

---

### Xenomorph Max Xp
**Author:**   
**Notes:** File: BLES01455-PROFILE\\PAYLOAD

```
search 0x03000C
write next (10):0x00039206
```

---

### Marine 99 Upgrade Points
**Author:**   
**Notes:** File: BLES01455-PROFILE\\PAYLOAD

```
write at 0x0000016D:0x63
```

---

### Marine Max Xp
**Author:**   
**Notes:** File: BLES01455-PROFILE\\PAYLOAD

```
search 0x03000C
write next (3):0x00039206
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
**Notes:** File: BLES01455-PROFILE\\PAYLOAD

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
