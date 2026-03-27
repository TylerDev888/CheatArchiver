# InviZimals_ Shadow Zone

**Console:** PSP  
**Region:** PAL  
**Serial:** UCES01411  
**Cheat Type:** Save Editor  
**Source:** [PSP](PSP)  

---

## Cheats

### Update Save Owner To Current Psp
**Author:**   
**Notes:** File: GAMEDATA

```
set [wlan]:host_wlan_addr
write at 0x0034:[wlan]
```

---

### Lock Save To Current Psp
**Author:**   
**Notes:** File: GAMEDATA

```
00000030 00000001
```

---

### Unlock Save To Any Psp
**Author:**   
**Notes:** File: GAMEDATA

```
00000030 00000000
```

---

### Update Custom Adler32 (required)
**Author:**   
**Notes:** File: GAMEDATA

```
write at 0x000C:0x99547688
set range:0x0000,EOF+1
set [hash]:Adler32:0x00000000
set [hash]:endian_swap
write at 0x000C:[hash]
```

---

### Update Murmur3-32 Hash (required)
**Author:**   
**Notes:** File: GAMEDATA

```
write at 0x000C:0x99547688
set range:0x0000,EOF+1
set [hash]:murmur3_32
set [hash]:endian_swap
write at 0x000C:[hash]
```

---
