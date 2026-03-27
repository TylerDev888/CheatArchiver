# Gundam Musou

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM60018  
**Cheat Type:** Save Editor  
**Source:** [Dynasty Warriors: Gundam](Dynasty Warriors: Gundam)  

---

## Cheats

### Update 1st Add For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN

```
set [csum]:0
set [csum]:add(0x000020,0x001FFF)
write at 0x000008:[csum]
```

---

### Update 2nd Add For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN

```
set [csum]:0
set [csum]:add(0x001DD0,0x07FDCF)
write at 0x00000C:[csum]
```

---

### Update 3rd Add For Data.bin (required)
**Author:**   
**Notes:** File: DATA.BIN  (set [csum]:add(0x000020,0x07FFFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000020,pointer)
write at 0x000010:[csum]
```

---
