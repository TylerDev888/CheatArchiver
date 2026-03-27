# Streets of Rage 2 (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00508  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000004,0x0B84E1)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
