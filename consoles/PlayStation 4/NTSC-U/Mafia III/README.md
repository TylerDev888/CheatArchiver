# Mafia III

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA03617  
**Cheat Type:** AP  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Wallet $99999999
**Author:**   
**Notes:** File: *

```
search \
write next 0x3C:0xFFE0F505
```

---

### Stash $99999999
**Author:**   
**Notes:** File: *

```
search \
write next 0x4C:0xFFE0F505
```

---

### 6 Medkits
**Author:**   
**Notes:** File: *

```
search \
write next 0x4E1:0x06000000
```

---

### Max Weapon 1 Bullets
**Author:**   
**Notes:** File: *

```
search \
write next 0xDB:0xFFE0F505
```

---

### Max Weapon 1 Clips
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0x47:0xFFE0F505
```

---

### Max Weapon 2 Bullets
**Author:**   
**Notes:** File: *

```
search \
write next 0x1DF:0xFFE0F505
```

---

### Max Weapon 2 Clips
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0x17F:0xFFE0F505
```

---

### 7 Frag Grenades
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0x117:0x07000000
```

---

### 5 Molotov Cocktails
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0xAF:0x05000000
```

---

### 7 Proximity Mines
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0x7B:0x07000000
```

---

### 7 Screaming Zemi
**Author:**   
**Notes:** File: *

```
search 0x066D5F416D6D6F
write next 0xE3:0x07000000
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: *

```
set pointer:EOF-3
set range:0x0000,pointer
set [hash]:CRC32
set [hash]:endian_swap
write next (0):[hash]
```

---
