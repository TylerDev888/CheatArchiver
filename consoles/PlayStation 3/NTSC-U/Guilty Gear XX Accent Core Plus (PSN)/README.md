# Guilty Gear XX Accent Core Plus (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30957  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Wadd For System.dat(required)
**Author:**   
**Notes:** File: SYSTEM.DAT  (set [csum]:wadd(0x000004,0x002AF7)) (Missing another checksum info which at address 0x04)

```
set pointer:EOF+1
set [csum]:wadd(0x000004,pointer)
set [csum]:right([csum],2)
write at 0x00:[csum]
```

---
