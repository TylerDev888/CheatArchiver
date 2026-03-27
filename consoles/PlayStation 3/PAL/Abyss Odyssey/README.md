# Abyss Odyssey

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01910  
**Cheat Type:** Save Editor  
**Source:** [Cheats by ed-209](Cheats by ed-209)  

---

## Cheats

### Decompress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Decompress(0x00000018, 15)
```

---

### Global Max Money
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x0000034B:0x3B9AC9FF
```

---

### Katrien Max Level 70
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000A7E:0x022BEC
```

---

### Katrien Max Skill Points
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000747:0x63
```

---

### Ghost Monk Max Level 70 (apply Only After Character Unlock)
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000AEC:0x022BEC
```

---

### Ghost Monk Max Skill Points (apply Only After Character Unlock)
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000794:0x63
```

---

### Pincoya Max Level 70 (apply Only After Character Unlock)
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000B5A:0x022BEC
```

---

### Pincoya Skill Max Points (apply Only After Character Unlock)
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x000007E1:0x63
```

---

### Compress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Compress(0x00000018)
```

---

### Sha1 For Payload By Chaoszage (required)
**Author:**   
**Notes:** File: NPUB31397-PROFILE\\PAYLOAD  (set range:0x000014,0x000201)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
