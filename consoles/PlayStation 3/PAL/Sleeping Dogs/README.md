# Sleeping Dogs

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01661  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big For Tcgs* (required)
**Author:**   
**Notes:** File: TCGS*  (set range:0x34,0x003EEF) (write at 0x003EF0:[hash])

```
set pointer:eof-3
set range:0x34,pointer
set [hash]:CRC32Big
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---

### Update Crc32big For Tcas (required)
**Author:**   
**Notes:** File: TCAS  (set range:0x34,0x007BC7) (write at 0x007BC8:[hash])

```
set pointer:eof-3
set range:0x34,pointer
set [hash]:CRC32Big
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---
