# Dynasty Warriors_ Gundam

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00147  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Pilot Points
**Author:**   
**Notes:** [Amuro Ray]  File: BLES00147-*\\DATA.BIN

```
20000188 05F5E0FF
```

---

### Level 30
**Author:**   
**Notes:** [Amuro Ray]  File: BLES00147-*\\DATA.BIN

```
00000198 0000001D
```

---

### Have All Skills
**Author:**   
**Notes:** [Amuro Ray]  File: BLES00147-*\\DATA.BIN

```
400001A5 000000FF
40070001 00000000
```

---

### Max Mobile Suit Points
**Author:**   
**Notes:** [Amuro Ray-gundam]  File: BLES00147-*\\DATA.BIN

```
20000020 0098967F
```

---

### Level 10
**Author:**   
**Notes:** [Amuro Ray-gundam]  File: BLES00147-*\\DATA.BIN

```
00000032 00000009
```

---

### Update Add For Data.bin (required)
**Author:**   
**Notes:** File: BLES00147-*\\DATA.BIN  (set [csum]:add(0x000020,0x088FFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000020,pointer)
write at 0x000010:[csum]
set [csum]:0
set [csum]:add(0x000020,0x001FFF)
write at 0x000008:[csum]
set [csum]:0
set [csum]:add(0x001DD1,0x088DCF)
write at 0x00000C:[csum]
```

---
