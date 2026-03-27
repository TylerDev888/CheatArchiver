# Mass Effect 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01462  
**Cheat Type:** Save Editor  
**Source:** [From zeick](From zeick)  

---

## Cheats

### Renegade
**Author:**   
**Notes:** File: SAVE*

```
search 0x000027B0
write next (4):00000063
```

---

### Paragon
**Author:**   
**Notes:** File: SAVE*

```
search 0x000027AF
write next (4):00000063
```

---

### Reputation
**Author:**   
**Notes:** File: SAVE*

```
search 0x0000288C
write next (4):00000063
```

---

### Medi Gel 9999999
**Author:**   
**Notes:** File: SAVE*

```
search \
write next (-64):0098967F
```

---

### Money 9999999
**Author:**   
**Notes:** File: SAVE*

```
search \
write next (-68):0098967F
```

---

### Export - Update Crc32big (required)
**Author:**   
**Notes:** File: EXPORT

```
set pointer:eof-3
set range:0x0, pointer
set [crc]:crc32big
set pointer:eof-3
write next (0):[crc]
```

---

### Quick - Update Crc32big (required)
**Author:**   
**Notes:** File: QUICK

```
set pointer:eof-3
set range:0x0, pointer
set [crc]:crc32big
set pointer:eof-3
write next (0):[crc]
```

---

### Legend - Update Crc32big (required)
**Author:**   
**Notes:** File: LEGEND

```
set pointer:eof-3
set range:0x0, pointer
set [crc]:crc32big
set pointer:eof-3
write next (0):[crc]
```

---

### Save - Update Crc32big (required)
**Author:**   
**Notes:** File: SAVE*

```
set pointer:eof-3
set range:0x0, pointer
set [crc]:crc32big
set pointer:eof-3
write next (0):[crc]
```

---
