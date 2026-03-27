# Legend of the Guardians_ The Owls of Ga'Hoole

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00964  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Save0.dat (required)
**Author:**   
**Notes:** File: SAVE0.DAT  (set range:0x000004,0x014003)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
