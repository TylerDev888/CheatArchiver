# Cabela's Survival_ Shadows of Katmai

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30819  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc-16 Ccitt (required)
**Author:**   
**Notes:** File: USRDATA  (set range:0x000000,0x103FFB) (write at 0x103FFE:[hash])

```
set crc_bandwidth:16
set crc_polynomial:0x1021
set crc_initial_value:0xFFFF
set crc_output_xor:0
set crc_reflection_input:0
set crc_reflection_output:0
set pointer:eof-3
set range:0x000000,pointer
set [hash]:crc
set pointer:eof-1
write next (0):[hash]
```

---
