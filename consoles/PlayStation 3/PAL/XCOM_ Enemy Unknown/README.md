# XCOM_ Enemy Unknown

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01711  
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

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x000450)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
