# Brave_ The Video Game

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01542  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie PS3](From Game Genie PS3)  

---

## Cheats

### Max Coins
**Author:**   
**Notes:** File: BRAVE0

```
2000062C 3B9AC9FF
```

---

### Update Crc32 For Brave0 (required)
**Author:**   
**Notes:** File: BRAVE0  (set range:0x00000C,0x0006E2)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
