# Shaun White Snowboarding

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00403  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc-16 Ccitt For Default.sav (required)
**Author:**   
**Notes:** File: DEFAULT.SAV  (set range:0x0000BC,0x044D15)

```
set crc_bandwidth:16
set crc_polynomial:0x1021
set crc_initial_value:0xFFFF
set crc_output_xor:0
set crc_reflection_input:0
set crc_reflection_output:0
set pointer:eof+1
set range:0x0000BC,pointer
set [hash]:crc
write at 0x00000C:[hash]
```

---
