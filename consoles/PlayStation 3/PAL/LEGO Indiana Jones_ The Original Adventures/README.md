# LEGO Indiana Jones_ The Original Adventures

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00254  
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
28000088 000000E8
2800008C D4A50FFF
```

---

### Update Dwadd For Savedata.dat(required)
**Author:**   
**Notes:** File: SAVEDATA.DAT  (set [csum]:dwadd(0x000000,0x007F7F)) (write at 0x0x007F80:[csum])

```
set pointer:EOF-4
set [csum]:0x5C0999
set [csum]:dwadd(0x000000,pointer)
set pointer:EOF-3
write next 0:[csum]
```

---
