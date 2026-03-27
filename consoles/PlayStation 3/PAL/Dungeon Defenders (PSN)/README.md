# Dungeon Defenders (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00652  
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

### Update Crc32big For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x009D81)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:CRC32Big
write at 0x000010:[hash]
```

---
