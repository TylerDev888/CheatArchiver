# Prototype

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00269  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Current Evolution Points
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20000C24 0098967F
200012A4 0098967F
```

---

### Max Total Evolution Points Collected
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20001BA0 0098967F
```

---

### Max Hydras Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200007E4 000F423F
```

---

### No Hydras Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200007E4 00000000
```

---

### Max Alerts Caused
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
2000083C 000F423F
```

---

### No Alerts Caused
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
2000083C 00000000
```

---

### Max Deaths
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20000968 000F423F
```

---

### No Deaths
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20000968 00000000
```

---

### Max Hunters Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20001628 000F423F
```

---

### No Hunters Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20001628 00000000
```

---

### Max Infected Water Towers Destroyed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20001664 000F423F
```

---

### No Infected Water Towers Destroyed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20001664 00000000
```

---

### Max Infected Hives Destroyed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200022A0 000F423F
```

---

### No Infected Hives Destroyed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200022A0 00000000
```

---

### Max Infected Civilians Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20002B54 000F423F
```

---

### No Infected Civilians Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20002B54 00000000
```

---

### Max Alerts Escaped
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20002D1C 000F423F
```

---

### No Alerts Escaped
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
20002D1C 00000000
```

---

### Max Evolved Infected Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200037B4 000F423F
```

---

### No Evolved Infected Killed
**Author:**   
**Notes:** File: BLES00269-DATA-*\\USERDATA.BIN

```
200037B4 00000000
```

---

### Init Custom Crc32 For Crc.bin (required)
**Author:**   
**Notes:** [Checksum]  File: ICON0.PNG

```
set crc_bandwidth:32
set crc_polynomial:0x04C11DB7
set crc_initial_value:0xFFFFFFFF
set crc_output_xor:0
set crc_reflection_input:0
set crc_reflection_output:0
set range:0x0000,eof+1
set [crc_init]:crc
```

---

### Calculate Custom Crc32 For Crc.bin (required)
**Author:**   
**Notes:** [Checksum]  File: USERDATA.BIN

```
set crc_bandwidth:32
set crc_polynomial:0x04C11DB7
set crc_initial_value:[crc_init]
set crc_output_xor:0
set crc_reflection_input:0
set crc_reflection_output:0
set range:0x0000,eof+1
set [hash]:crc
```

---

### Update Custom Crc32 For Crc.bin (required)
**Author:**   
**Notes:** [Checksum]  File: CRC.BIN

```
write at 0x0:[hash]
```

---
