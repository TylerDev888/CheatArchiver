# Sonic & All-Stars Racing Transformed

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01646  
**Cheat Type:** Save Editor  

---

## Cheats

### Update 1 Dwadd For Profile.dat (required)
**Author:**   
**Notes:** File: PROFILE.DAT  (set [csum]:dwadd(0x10,0x0927FF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x10,pointer)
write at 0x000008:[csum]
```

---

### Update 2 Dwadd For Profile.dat (required)
**Author:**   
**Notes:** File: PROFILE.DAT  (set [csum]:dwadd(0x000004,0x0A5FFF))

```
set [csum]:0
set pointer:eof+1
set [csum]:dwadd(0x000004,pointer)
write at 0x000000:[csum]
```

---
