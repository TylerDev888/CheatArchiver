# CASTLE OF ILLUSION_ Starring Mickey Mouse

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01427  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Adler32 For Metagame.dat (required)
**Author:**   
**Notes:** File: METAGAME.DAT

```
set [size]:read(8,4)
set [begin]:0xC
set [end_range]:[begin]+[size]-1
set range:[begin],[end_range]
set [hash]:Adler32
write at 0x000004:[hash]
```

---
