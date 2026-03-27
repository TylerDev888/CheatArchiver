# Dynasty Warriors_ Gundam 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00528  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Level 30
**Author:**   
**Notes:** [Amuro Ray]  File: BLES00528-*\\DATA.BIN

```
00000173 0000001D
```

---

### Max Pilot Points
**Author:**   
**Notes:** [Amuro Ray]  File: BLES00528-*\\DATA.BIN

```
20000174 05F5E0FF
```

---

### Update Add For Data.bin (required)
**Author:**   
**Notes:** File: BLES00528-*\\DATA.BIN  (set [csum]:add(0x000020,0x0A3FFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000020,pointer)
write at 0x000010:[csum]
```

---
