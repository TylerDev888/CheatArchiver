# Resistance 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES01118  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Unlock All Levels
**Author:**   
**Notes:** File: BCES01118_SAVE_*\\GAME.SAV

```
10002C6C 0000FFFF
42002C6E 03030303
40B00004 00000000
```

---

### Have All Cinematics
**Author:**   
**Notes:** [Extras]  File: BCES01118_SAVE_*\\GAME.SAV

```
42002F50 FFFFFFFF
40030004 00000000
```

---

### Have All Journals
**Author:**   
**Notes:** [Extras]  File: BCES01118_SAVE_*\\GAME.SAV

```
42004670 FFFFFFFF
40070004 00000000
```

---

### Have All Cheats Purchased()
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
00004742 000000FF
```

---

### Have All Skins Purchased()
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
00004746 0000000F
```

---

### Have All Art Purchased()
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
20004748 FFFFFFFF
```

---

### Have All Titles Purchased
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
42004753 FFFFFFFF
40030004 00000000
```

---

### Have All Videos
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
00004752 000000FF
```

---

### Unlock All Cheats And Videos
**Author:**   
**Notes:** [Shop]  File: BCES01118_SAVE_*\\GAME.SAV

```
000046A8 000000FF
```

---

### Max Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
00003DDC 00000001
```

---

### Max Headshot Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
200043CC FFFFFFFF
```

---

### Max Total Gibs
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
0000468D 000000FF
0000468E 000000FF
```

---

### Max Military Chimera Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
00003FC0 000000FF
```

---

### Max Feral Chimera Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
00003FD0 000000FF
```

---

### Max Mech Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
00003FE0 000000FF
```

---

### Max Human Kills
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
20003FEC FFFFFFFF
```

---

### No Deaths
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
20004330 00000000
```

---

### Reset Time Played
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
200043D0 00000000
200043D4 00000000
```

---

### Max Number Of Intel Collected
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
0000468B 000000FF
0000468C 000000FF
```

---

### Max Weapons Stats
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV

```
40003DA9 000000FF
40090010 00000000
00003DC1 000000FF
00003E21 000000FF
00003E49 000000FF
```

---

### Update Crc32 For Game.sav (required)
**Author:**   
**Notes:** [Statistics]  File: BCES01118_SAVE_*\\GAME.SAV  (set range:0x000020,0x007E67)

```
set pointer:EOF-7
set range:0x20,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x00000C:[hash]
```

---
