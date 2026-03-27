# Leisure Suit Larry_ Box Office Bust

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00553  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32big (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000008,0x006523)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---
