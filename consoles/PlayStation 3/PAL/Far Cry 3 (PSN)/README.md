# Far Cry 3 (PSN)

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** NPEB01096  
**Cheat Type:** Save Editor  
**Source:** [From KE-HA](From KE-HA)  

---

## Cheats

### Infinite Ammo
**Author:**   
**Notes:** File: SAVEDATA.000

```
80010004 C4109701
08000004 00000001
80010004 E2B37D01
08000004 00000001
80010004 4A2F3E01
08000004 00000001
```

---

### Wallet Size 99999999
**Author:**   
**Notes:** File: SAVEDATA.000

```
80010005 550B36AD
04000000 00000000
28000005 7F969800
```

---

### Money 99999999
**Author:**   
**Notes:** File: SAVEDATA.000

```
80010008 F7C201E0
3C1E7604 00000000
28000008 7F969800
```

---

### Update Md5 Hashes (required)
**Author:**   
**Notes:** File: SAVEDATA.000

```
search 0xA8110000
set range:0x30, pointer+3
set [md5]:md5
write at 0x10:[md5]
```

---
