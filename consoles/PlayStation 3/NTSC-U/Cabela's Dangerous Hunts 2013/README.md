# Cabela's Dangerous Hunts 2013

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31009  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc-16 Ccitt For Save.ces (required)
**Author:**   
**Notes:** File: SAVE.CES  (set range:0x000048,0x07F1A7)

```
set crc_bandwidth:16
set crc_polynomial:0x1021
set crc_initial_value:0xFFFF
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:0
set crc_reflection_output:0
set pointer:eof+1
set range:0x000048,pointer
set [hash]:crc
write at 0x00002B:[hash]
```

---
