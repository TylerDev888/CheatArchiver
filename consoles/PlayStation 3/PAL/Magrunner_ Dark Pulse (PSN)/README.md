# Magrunner_ Dark Pulse (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01280  
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
**Notes:** File: PAYLOAD  (set range:0x000018,0x002ED7)

```
set pointer:eof+1
set range:0x000018,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
