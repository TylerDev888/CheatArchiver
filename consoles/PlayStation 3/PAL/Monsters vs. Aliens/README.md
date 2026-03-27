# Monsters vs. Aliens

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00490  
**Cheat Type:** Save Editor  
**Source:** [From chaoszage](From chaoszage)  

---

## Cheats

### 99999999 Dna Points
**Author:**   
**Notes:** File: GAMEDATA

```
write at 0x44:05F5E0FF
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: GAMEDATA  (set range:0x000004,0x000AA3)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
