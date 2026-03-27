# FIFA 14

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01876  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 In Data0000
**Author:**   
**Notes:** File: DATA0000

```
set pointer:eof+1
set range:0x1C,pointer
set [hash]:crc32
write at 0x10:[hash]
```

---

### Get Crc32 For Data0000
**Author:**   
**Notes:** File: DATA0000

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0xFFFFFFFF
set crc_output_xor:0
set crc_reflection_input:1
set crc_reflection_output:0
set pointer:eof+1
set range:0x1C,pointer
set [hash]:crc
```

---

### Get Crc32 For Data0001
**Author:**   
**Notes:** File: DATA0001

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:[hash]
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set pointer:eof+1
set range:0x0,pointer
set [hash]:crc
```

---

### Get Crc32 For Data0002
**Author:**   
**Notes:** File: DATA0002

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:[hash]
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set pointer:eof+1
set range:0x0,pointer
set [hash]:crc
```

---
