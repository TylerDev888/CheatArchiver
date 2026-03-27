# Digimon all-star rumble

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31441  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Bits Money
**Author:**   
**Notes:** File: SAVEDATA

```
write next 0x10A:0x7FFFFFFF
```

---

### Checksum32 (signed) Hashes (required)
**Author:**   
**Notes:** File: SAVEDATA  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes)

```
write at 0x14:0x00000000
set range:0x0,0x185D
set [num]:Checksum32
write at 0x14:[num]
```

---
