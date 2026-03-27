# SIREN_ New Translation

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BCJS30020  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Siren.dat (required)
**Author:**   
**Notes:** File: SIREN.DAT  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x0,0x000477)

```
write at 0x00000C:00000000
set pointer:eof+1
set range:0x0,pointer
set [hash]:CRC32
set [hash]:xor:FFFFFFFF
write at 0x00000C:[hash]
```

---
