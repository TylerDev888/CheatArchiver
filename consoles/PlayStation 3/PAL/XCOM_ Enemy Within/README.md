# XCOM_ Enemy Within

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01851  
**Cheat Type:** Save Editor  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Decompress(*, 15)
```

---

### Compress Save (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Compress(*)
```

---

### Update Crc32big For Save Payload (required)
**Author:**   
**Notes:** File: BLES01851-SAVE1\\PAYLOAD  (set range:0x400,0x0172EC)

```
set pointer:eof+1
set range:0x400,pointer
set [hash]:CRC32Big
write at 0x0000C1:[hash]
```

---

### Update Sha1 For Profile Payload (required)
**Author:**   
**Notes:** File: BLES01851-PROFILE\\PAYLOAD  (set range:0x000014,0x00070F)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
