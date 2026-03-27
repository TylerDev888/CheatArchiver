# Mars_ War Logs (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01301  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Md2 For Savedata (required)
**Author:**   
**Notes:** File: SAVEDATA  (set range:0x00000A,0x0250C0)

```
set pointer:eof+1
set range:0x00000A,pointer
set [hash]:MD2
write at 0x000005:[hash]
```

---
