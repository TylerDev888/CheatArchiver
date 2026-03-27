# LEGO Indiana Jones 2_ The Adventure Continues

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00763  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Studs
**Author:**   
**Notes:** File: SAVEDATA.DAT

```
8001000C 45610000
00000000 00000000
28000108 000000E8
2800010C D4A50FFF
```

---

### Update Dwadd For Savedata.dat(required)
**Author:**   
**Notes:** File: SAVEDATA.DAT

```
set [csum]:0x5C0999
set [csum]:dwadd(0x000000,0x0813DF)
write at 0x0813E0:[csum]
```

---
