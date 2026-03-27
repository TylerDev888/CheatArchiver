# Spec Ops_ The Line

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01157  
**Cheat Type:** AP  

---

## Cheats

### Decompress Save (required)
**Author:**   
**Notes:** File: PAYLOAD0

```
Decompress(*, 15)
```

---

### Compress Save (required)
**Author:**   
**Notes:** File: PAYLOAD0

```
Compress(*)
```

---

### Update Sha1 (required)
**Author:**   
**Notes:** File: PAYLOAD0  (set range:0x000014,0x0004DB)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---

### Update Sha1 For Payload0 (required)
**Author:**   
**Notes:** File: PAYLOAD0  (set range:0x000014,0x0004DB)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
