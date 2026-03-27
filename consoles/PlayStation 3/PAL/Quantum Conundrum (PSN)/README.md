# Quantum Conundrum (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00895  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big For Profile.qcp (required)
**Author:**   
**Notes:** File: PROFILE.QCP  (set range:0x000008,0x000533)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---

### Update Sha1 For Profile.qcp (required)
**Author:**   
**Notes:** File: PROFILE.QCP  (set range:0x00001C,0x0003BA)

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:SHA1
write at 0x000008:[hash]
```

---
