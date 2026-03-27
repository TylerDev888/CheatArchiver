# Assassin's Creed III

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01667  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: BLES01667AC3AC3_*\\AC3_*

```
80010004 A657F804
280000A7 FFE0F505
80010004 7FC985D9
280000A7 FFE0F505
```

---

### Update Custom Crc32 Ac3_0.sav (required)
**Author:**   
**Notes:** File: BLES01667AC3AC3_*\\AC3_*

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0xBAE23CD0
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set [size]:read(0x00,4)
set range:0x0008,[size]+7
set [hash]:crc
write at 0x0004:[hash]
```

---

### Update Custom Crc32 Options (required)
**Author:**   
**Notes:** File: OPTIONS

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0xBAE23CD0
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set [size]:read(0x00,4)
set range:0x0008,[size]+7
set [hash]:crc
write at 0x0004:[hash]
```

---
