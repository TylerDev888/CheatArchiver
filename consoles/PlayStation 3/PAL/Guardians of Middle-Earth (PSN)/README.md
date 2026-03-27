# Guardians of Middle-Earth (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01085  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Add For Filename.sav (required)
**Author:**   
**Notes:** File: FILENAME.SAV  (set [csum]:add(0x000000,0x00FC2E)) (write at 0x00FC2F:[csum])

```
set [csum]:0
set pointer:eof-4
set [csum]:add(0x000000,pointer)
set pointer:eof-3
write next (0):[csum]
```

---
