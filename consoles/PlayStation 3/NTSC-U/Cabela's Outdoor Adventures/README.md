# Cabela's Outdoor Adventures

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30409  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc-16 Ccitt For Usrdata (required)
**Author:**   
**Notes:** File: USRDATA  (write at 0x027FFE:[hash])

```
set crc_bandwidth:16
set crc_polynomial:0x1021
set crc_initial_value:0xFFFF
set crc_output_xor:0
set crc_reflection_input:0
set crc_reflection_output:0
set range:0x000000,0x027FFB
set [hash]:crc
set pointer:eof-1
write next (0):[hash]
```

---
