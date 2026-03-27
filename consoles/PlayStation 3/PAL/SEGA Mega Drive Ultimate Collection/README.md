# SEGA Mega Drive Ultimate Collection

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00475  
**Cheat Type:** Save Editor  

---

## Cheats

### 999,999 Gold
**Author:**   
**Notes:** [Shining Force]  File: PAYLOAD

```
write at 0x00009D3C:0x0F423F
```

---

### Main Character 255 Hp 99 Mp
**Author:**   
**Notes:** [Shining Force]  File: PAYLOAD

```
write at 0x00009D51:0x00FF00FF
write at 0x00009D55:0x6363
```

---

### Main Character Chaos Breaker & Kindan Nohako
**Author:**   
**Notes:** [Shining Force]  File: PAYLOAD

```
write at 0x00009D59:0xA75CFFFF
```

---

### Main Character Aura 4 & Bolt 4
**Author:**   
**Notes:** [Shining Force]  File: PAYLOAD

```
write at 0x00009D5D:0x0DC1CBFF
```

---

### Main Character 99 Atk.def.mov.agi.
**Author:**   
**Notes:** [Shining Force]  File: PAYLOAD

```
write at 0x00009D4B:0x63636363
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x0B8481)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
