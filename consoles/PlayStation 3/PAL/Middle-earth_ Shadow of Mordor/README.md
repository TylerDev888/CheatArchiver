# Middle-earth_ Shadow of Mordor

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01745  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Upgrades Pts
**Author:**   
**Notes:** File: FILENAME.SAV

```
search 0xC8DAA7A504:2
write next (-6):0x0003E7
```

---

### Max Mirian Money
**Author:**   
**Notes:** File: FILENAME.SAV

```
search 0xECFD4156:2
write next (+1):0x0000270F
```

---

### Update Add For Filename.sav (required)
**Author:**   
**Notes:** File: FILENAME.SAV  (set [csum]:add(0x000010,0x0FFFFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000010,pointer)
write at 0x000008:[csum]
```

---
