# Far Cry 3_ Blood Dragon

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01322  
**Cheat Type:** Save Editor  
**Source:** [From zeick](From zeick)  

---

## Cheats

### Xp 7900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):DC1E0000
```

---

### Xp 8400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):D0200000
```

---

### Xp 8900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):C4220000
```

---

### Xp 9400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):B8240000
```

---

### Xp 9900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):AC260000
```

---

### Xp 10400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):A0280000
```

---

### Xp 10900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):942A0000
```

---

### Xp 11400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):882C0000
```

---

### Xp 11900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):7C2E0000
```

---

### Xp 12400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):70300000
```

---

### Xp 12900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):64320000
```

---

### Xp 13400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):58340000
```

---

### Xp 13900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):4C360000
```

---

### Xp 14400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):40380000
```

---

### Xp 14900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):343A0000
```

---

### Xp 15400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):283C0000
```

---

### Xp 15900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):1C3E0000
```

---

### Xp 16400
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):10400000
```

---

### Xp 16900
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xFB64928A
write next (-4):04420000
```

---

### Money 10000000
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xA4F7C201E03C1E7604
write next (9):80969800
```

---

### Inf Ammo
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xC4109701
write next (4):01
search 0xE2B37D01
write next (4):01
search 0x4A2F3E01
write next (4):01
```

---

### Infinite Ammo
**Author:**   
**Notes:** File: SAVEDATA.000  ([Update md5 hashes (required)]) (set [end]:read(0xC,4)) (set [end]:[end]+0x2F) (set range:0x30,[end]) (set [md5]:md5) (write at 0x10:[md5])

```
80010004 C4109701
08000004 00000001
80010004 E2B37D01
08000004 00000001
80010004 4A2F3E01
08000004 00000001
```

---

### Update Crc32 & Md5 Hashes (required)
**Author:**   
**Notes:** File: SAVEDATA.000

```
set pointer:read(0xC,4)
set pointer:pointer+2F
set range:0x30, pointer
set [md5]:md5
write at 0x10:[md5]
set pointer:read(0xC,4)
set pointer:pointer+2F
set range:0x30, pointer
set [crc]:crc32
write at 0x20:[crc]
```

---
