# LEGO Lord Of The Rings

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01516  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Studs
**Author:**   
**Notes:** File: GAME1

```
8001000C 45610000
00000000 00000000
28000118 000000E8
2800011C D4A50FFF
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
