# The Lord of the Rings_ Aragorn's Quest

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00998  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Lotr.dat (required)
**Author:**   
**Notes:** File: LOTR.DAT  (set range:0x000000,0x03E393) (write at 0x03E394:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---

### Update Crc32 For Cutsflag.dat (required)
**Author:**   
**Notes:** File: CUTSFLAG.DAT  (set range:0x000000,0x000137) (write at 0x000138:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
set pointer:eof-3
write next (0):[hash]
```

---
