# Planet Minigolf (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB00163  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Data (required)
**Author:**   
**Notes:** File: DATA  (set range:0x000000,0x0015B5) (write at 0x0015B6:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next (0):[hash]
```

---
