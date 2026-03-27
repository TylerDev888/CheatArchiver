# LEGO Batman_ The Videogame

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00332  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Studs
**Author:**   
**Notes:** File: SAVEDATA.DAT

```
80010008 45610000
000186A0 00000000
28000094 000000E8
28000098 D4A50FFF
```

---

### Update Dwadd For Savedata.dat(required)
**Author:**   
**Notes:** File: SAVEDATA.DAT  (set [csum]:dwadd(0x000000,0x007E1B)) (write at 0x0x007E1C:[csum])

```
set pointer:EOF-4
set [csum]:0x5C0999
set [csum]:dwadd(0x000000,pointer)
set pointer:EOF-3
write next 0:[csum]
```

---
