# Like a Dragon_ Ishin!

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA32171  
**Cheat Type:** AP  
**Source:** [encryption/checksum/codes by bucanero](encryption/checksum/codes by bucanero)  

---

## Cheats

### Decrypt Data.ps4.sav (required)
**Author:**   
**Notes:** File: data.ps4.sav

```
set pointer:EOF-0x0F
set range:0x00,pointer
DECRYPT rgg_studio(\
```

---

### 9999999 Virtue
**Author:**   
**Notes:** File: data.ps4.sav

```
20017738 0098967F
```

---

### 9999999 Money
**Author:**   
**Notes:** File: data.ps4.sav

```
20017708 0098967F
```

---

### 99 Blue Swordman Orbs
**Author:**   
**Notes:** File: data.ps4.sav

```
00007428 00000063
```

---

### 99 Yellow Gunman Orbs
**Author:**   
**Notes:** File: data.ps4.sav

```
00007429 00000063
```

---

### 99 Green Wild Dancer Orbs
**Author:**   
**Notes:** File: data.ps4.sav

```
0000742A 00000063
```

---

### 99 Red Brawler Orbs
**Author:**   
**Notes:** File: data.ps4.sav

```
0000742B 00000063
```

---

### 99 Grey Training Orbs
**Author:**   
**Notes:** File: data.ps4.sav

```
0000742C 00000063
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: data.ps4.sav

```
set pointer:EOF-0x0F
set range:0x00,pointer
set [crc]:crc32
set [crc]:endian_swap
write next 0x08:[crc]
```

---

### Encrypt Data.ps4.sav (required)
**Author:**   
**Notes:** File: data.ps4.sav

```
set pointer:EOF-0x0F
set range:0x00,pointer
ENCRYPT rgg_studio(\
```

---
