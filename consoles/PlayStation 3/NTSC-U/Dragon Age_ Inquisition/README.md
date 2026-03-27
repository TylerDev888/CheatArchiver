# Dragon Age_ Inquisition

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30997  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

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
