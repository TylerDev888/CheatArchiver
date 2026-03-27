# Assassin's Creed II

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00669  
**Cheat Type:** Save Editor  
**Source:** [crc checksum by Devildwarf](crc checksum by Devildwarf)  

---

## Cheats

### Enable Auditore Crypt Uplay Map
**Author:**   
**Notes:** File: OPTIONS

```
00000498 00000001
```

---

### Enable Uplay Altairs Outfit
**Author:**   
**Notes:** File: OPTIONS

```
00000486 00000001
```

---

### Enable Uplay Knives Upgrade
**Author:**   
**Notes:** File: OPTIONS

```
00000474 00000001
```

---

### Enable Verizon App Store Bonus Skin
**Author:**   
**Notes:** File: OPTIONS

```
0000041A 00000001
```

---

### Enable Maria Thorpe Longsword
**Author:**   
**Notes:** File: OPTIONS

```
0000056B 00000001
```

---

### Enable Fredricks Hammer
**Author:**   
**Notes:** File: OPTIONS

```
0000056C 00000001
```

---

### Enable Mace Of The Bull
**Author:**   
**Notes:** File: OPTIONS

```
0000056D 00000001
```

---

### Enable Dark Oracle Bone Dagger
**Author:**   
**Notes:** File: OPTIONS

```
0000056E 00000001
```

---

### Enable Twins Rapier
**Author:**   
**Notes:** File: OPTIONS

```
0000056F 00000001
```

---

### Enable Boucharts Blade
**Author:**   
**Notes:** File: OPTIONS

```
00000570 00000001
```

---

### Update Custom Crc32 Options (required)
**Author:**   
**Notes:** File: OPTIONS

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0
set crc_output_xor:0x1BF3278A
set crc_reflection_input:1
set crc_reflection_output:1
set [size]:read(0x00,4)
set range:0x0008,[size]+7
set [hash]:crc
write at 0x0004:[hash]
```

---

### Update Custom Crc32 Ac2_0.sav (required)
**Author:**   
**Notes:** File: AC2_0.SAV

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
