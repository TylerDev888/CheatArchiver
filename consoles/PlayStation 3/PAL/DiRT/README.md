# DiRT

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00095  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Dwadd For Savedata (required)
**Author:**   
**Notes:** File: SAVEDATA  (set [csum]:dwadd(0x000008,0x06FB6B))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000008,pointer)
write at 0x000000:[csum]
```

---
