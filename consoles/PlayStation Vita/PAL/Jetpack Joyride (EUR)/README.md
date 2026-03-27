# Jetpack Joyride (EUR)

**Console:** PlayStation Vita  
**Region:** PAL  
**Serial:** PCSB00244  
**Cheat Type:** Save Editor  
**Source:** [Credits: Slade](Credits: Slade)  

---

## Cheats

### 9,999,999 Credits(\
**Author:**   
**Notes:** File: JETPACK.SAV

```
20000050 0098967F
```

---

### Update Crc32 For Jetpack.sav (required)
**Author:**   
**Notes:** File: JETPACK.SAV  (crc32 is stored in little-endian)

```
set pointer:eof+1
set range:0x04,pointer
set [crc]:crc32
set [crc]:endian_swap
write at 0x00:[crc]
```

---
