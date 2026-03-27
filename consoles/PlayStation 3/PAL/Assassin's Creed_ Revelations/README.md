# Assassin's Creed_ Revelations

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01384  
**Cheat Type:** Save Editor  
**Source:** [GameGenie EU Codes](GameGenie EU Codes)  

---

## Cheats

### Max Money
**Author:**   
**Notes:** File: BLES01384AC2AC2_*\\AC2_*.SAV

```
80010004 16A1923C
28000097 FFE0F505
```

---

### Update Custom Crc32 Ac2_0.sav (required)
**Author:**   
**Notes:** File: BLES01384AC2AC2_*\\AC2_*.SAV

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
