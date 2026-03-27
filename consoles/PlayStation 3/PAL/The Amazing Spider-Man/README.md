# The Amazing Spider-Man

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01547  
**Cheat Type:** Save Editor  
**Source:** [From Chris Roberts](From Chris Roberts)  

---

## Cheats

### Tech Upgrades (999999)
**Author:**   
**Notes:** File: GAMEDATA

```
2000C030 000F423F
```

---

### Enemies Defeated (9999)
**Author:**   
**Notes:** File: GAMEDATA

```
1000C3D6 0000270F
```

---

### Stealth Takedowns (255)
**Author:**   
**Notes:** File: GAMEDATA

```
1000C3DF 000000FF
```

---

### Update Crc32 For Gamedata (required)
**Author:**   
**Notes:** File: GAMEDATA  (set range:0x000004,0x00C523)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
