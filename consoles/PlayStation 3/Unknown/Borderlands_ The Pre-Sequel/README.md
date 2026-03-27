# Borderlands_ The Pre-Sequel

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10281  
**Cheat Type:** AP  

---

## Cheats

### Decompress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Decompress(0x00000018, 15)
```

---

### 9999999 Token
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
write at 0x00000320:0x98967F00
```

---

### Compress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Compress(0x00000018)
```

---

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x000166)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
