# The Bureau_ XCOM Declassified

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01322  
**Cheat Type:** Save Editor  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: BLES01322-XPROFILE\\PAYLOAD

```
Decompress(*, 15)
```

---

### Compress Save (required)
**Author:**   
**Notes:** File: BLES01322-XPROFILE\\PAYLOAD

```
Compress(*)
```

---

### Update Sha1 (required)
**Author:**   
**Notes:** File: BLES01322-XPROFILE\\PAYLOAD

```
set range:0x000014,0x031243
set [hash]:SHA1
write at 0x000000:[hash]
```

---

### Update Crc32big For Payload (required)
**Author:**   
**Notes:** File: BLES01322-XSAVEA1_0\\PAYLOAD  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x0,0x13CFEF)

```
write at 0x000004:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---
