# The House Of The Dead_ Overkill - Extended Cut

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01326  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: GAMESAVE

```
20000188 000F423F
```

---

### Have All Guns, Including The Unlockables(from Horrorolf)
**Author:**   
**Notes:** File: GAMESAVE

```
2000006C 00000F76
20000070 00000F76
```

---

### Update Crc32big:0 For Gamesave (required)
**Author:**   
**Notes:** File: GAMESAVE  (set range:0x000010,0x00402F)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000008:[hash]
set range:0x000000,0x00000B
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x00000C:[hash]
```

---
