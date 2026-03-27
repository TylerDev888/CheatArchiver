# INVERSION

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01495  
**Cheat Type:** Save Editor  
**Source:** [From chaoszage](From chaoszage)  

---

## Cheats

### 219999 Xp(by Chaoszage)
**Author:**   
**Notes:** File: SAVES.CFG  (Earn 1 xp to gain xp trophy)

```
search 0x56657273696F6E:1
set pointer:pointer+31
write next (0):0x00035B5F
```

---

### 429999 Xp
**Author:**   
**Notes:** File: SAVES.CFG  (Earn 1 xp to gain xp trophy)

```
search 0x56657273696F6E:1
set pointer:pointer+31
write next (0):0x00068FAF
```

---

### 799999 Xp
**Author:**   
**Notes:** File: SAVES.CFG  (Earn 1 xp to gain xp trophy)

```
search 0x56657273696F6E:1
set pointer:pointer+31
write next (0):0x000C34FF
```

---

### Update Crc32 For Saves.cfg (required)
**Author:**   
**Notes:** File: SAVES.CFG

```
set range:0x00000C,0x01F
set [hash]:CRC32
write at 0x8:[hash]
search 0x56657273696F6E:1
set [offset]:pointer+18
set range:0x0024,[offset]
set [hash]:CRC32
write at 0x0020:[hash]
set [start]:pointer+23
set [end]:pointer+389
set range:[start],[end]
set [hash]:CRC32
set pointer:pointer+19
write next (0):[hash]
```

---
