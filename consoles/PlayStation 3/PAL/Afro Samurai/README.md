# Afro Samurai

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00516  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Unlock All Treasures
**Author:**   
**Notes:** File: AFRO_0.SAV

```
420000E4 01010101
40130004 00000000
```

---

### Update Crc32:0 (required)
**Author:**   
**Notes:** File: AFRO_0.SAV

```
set pointer:eof-4
set range:0x000000,pointer
set [hash]:CRC32:0
set [hash]:xor:FFFFFFFF
set pointer:eof-4
write next (0):[hash]
```

---
