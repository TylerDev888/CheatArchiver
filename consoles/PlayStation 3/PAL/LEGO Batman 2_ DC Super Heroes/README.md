# LEGO Batman 2_ DC Super Heroes

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01613  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Studs
**Author:**   
**Notes:** File: GAME1

```
80010010 45610000
00000000 00000000
000186A0 00000000
28000108 000000E8
2800010C D4A50FFF
```

---

### Update Checksum For Game1 (required)
**Author:**   
**Notes:** File: GAME1

```
set pointer:eof+1
set range:0x10,pointer
set [hash]:fnv1:0xFFFFFFFF
set [hash]:xor:FFFFFFFF
write at 0x000C:[hash]
```

---
