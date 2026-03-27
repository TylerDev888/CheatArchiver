# Tony Hawk's Project 8

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00014  
**Cheat Type:** Save Editor  
**Source:** [From aldotools](From aldotools)  

---

## Cheats

### Update Crc32 For Abca1484.prg (required)
**Author:**   
**Notes:** File: ABCA1484.PRG  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (write at 0x000000:B22F5599)

```
write at 0x000000:00000000
set [eof]:read(0xC,4)
set [eof]:[eof]-1
set range:0x000000,[eof]
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
