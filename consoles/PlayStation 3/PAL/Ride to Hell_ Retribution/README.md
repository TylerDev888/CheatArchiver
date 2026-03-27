# Ride to Hell_ Retribution

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01581  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### Max Cash
**Author:**   
**Notes:** File: PAYLOAD

```
write at 0x00000E50:0x3B9AC9FF
write at 0x00001269:0x3B9AC9FF
write at 0x00001682:0x3B9AC9FF
```

---

### Update Crc32big For Payload (required)(from Zeick. Thank You!)
**Author:**   
**Notes:** File: PAYLOAD

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big
set pointer:eof-3
write next (0):[hash]
```

---

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: BLES01581-PROFILE\\PAYLOAD  (set range:0x000014,0x0000A7)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
