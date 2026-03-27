# Wolfenstein_ The New Order

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01909  
**Cheat Type:** Save Editor  
**Source:** [By Dark Nacho](By Dark Nacho)  

---

## Cheats

### Laserkraftwerk Max Ammo
**Author:**   
**Notes:** File: _MAPCHK0

```
search \
write next (70):0x270F
```

---

### Assualt Rifle 1960 Max Ammo
**Author:**   
**Notes:** File: _MAPCHK0

```
search \
write next (24):0xFF
search \
write next (24):0xFF
```

---

### Shotgun Ammo
**Author:**   
**Notes:** File: _MAPCHK0

```
search \
write next (15):0xFF
```

---

### Handgun Max Ammo *without Suppressor
**Author:**   
**Notes:** File: _MAPCHK0

```
search \
write next (15):0xFF
search \
write next (15):0xFF
```

---

### Update Md5_xor For _prof (required)
**Author:**   
**Notes:** File: _PROF  (set range:0x000000,0x000590) (write at 0x000591:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---

### Update Md5_xor For _mapstr0 (required)
**Author:**   
**Notes:** File: _MAPSTR0  (set range:0x000000,0x000BF2) (write at 0x000BF3:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---

### Update Md5_xor For _mapchk0 (required)
**Author:**   
**Notes:** File: _MAPCHK0  (set range:0x000000,0x00BCAE) (write at 0x00BCAF:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---
