# Assassin's Creed

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00158  
**Cheat Type:** Save Editor  
**Source:** [crc checksum by bucanero](crc checksum by bucanero)  

---

## Cheats

### Update Custom Crc32 Options.dat (required)
**Author:**   
**Notes:** File: OPTIONS.DAT

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0
set crc_output_xor:0x313F7650
set crc_reflection_input:1
set crc_reflection_output:1
set [size]:read(0x00,4)
set range:0x0008,[size]+7
set [hash]:crc
write at 0x0004:[hash]
```

---

### Update Custom Crc32 Savegame.dat (required)
**Author:**   
**Notes:** File: SAVEGAME.DAT

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
