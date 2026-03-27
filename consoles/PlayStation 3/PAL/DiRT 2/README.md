# DiRT 2

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00673  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For Savedata (required)
**Author:**   
**Notes:** File: SAVEDATA  (set [csum]:dwadd(0xC,0x01FFE7))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0xC,pointer)
set [csum]:xor:FFFFFFFF
write at 0x000000:[csum]
```

---
