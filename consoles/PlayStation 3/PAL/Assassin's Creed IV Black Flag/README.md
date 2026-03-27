# Assassin's Creed IV Black Flag

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01882  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Custom Crc32 Ac4_0.sav (required)
**Author:**   
**Notes:** File: AC4_0.SAV

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
