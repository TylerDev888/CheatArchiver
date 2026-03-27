# Need for Speed™ Rivals

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01894  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  (cheats should go here)

```
set range:0x000004,eof+1
DECRYPT blowfish_ecb(0x2391F201B36C85E81B1272D690FFA545)
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set range:0x000004,eof+1
ENCRYPT blowfish_ecb(0x2391F201B36C85E81B1272D690FFA545)
```

---

### Update Custom Crc32 For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set crc_bandwidth:32
set crc_polynomial:0x4C11DB7
set crc_initial_value:0xE195D3B7
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set range:0x00004,eof+1
set [hash]:crc
write at 0x0:[hash]
```

---
