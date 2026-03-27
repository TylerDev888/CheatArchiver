# Dragon's Dogma_ Dark Arisen

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01794  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Data0.dat (required)
**Author:**   
**Notes:** File: DATA0.DAT

```
set [end]:read(0x8,4)
set [end]:[end]+1F
set range:0x000020,[end]
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x000018:[hash]
```

---
