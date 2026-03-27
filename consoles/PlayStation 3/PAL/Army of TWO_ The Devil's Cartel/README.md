# Army of TWO_ The Devil's Cartel

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01767  
**Cheat Type:** Save Editor  
**Source:** [From KE-HA](From KE-HA)  

---

## Cheats

### Cash $999000
**Author:**   
**Notes:** File: USR-DATA

```
8001000A 57616C6C
65744361 73680000
2800000F 39393930
18000013 00003030
```

---

### Level 25(from X-ghost-x (using Bsd's Patch Creator))
**Author:**   
**Notes:** File: USR-DATA

```
search 0x000B436172656572436173680000000005
write at 0x000021E1:0x393939303030
```

---

### Max Career Cash & Bank Credit (alt)(works After Tutorial)
**Author:**   
**Notes:** File: USR-DATA

```
search \
write next (15):\
search \
write next (15):\
```

---

### Default:update Crc32 (required)
**Author:**   
**Notes:** File: USR-DATA

```
set range:0x4,0x63FFF
set [hash]:crc32
write at 0x0:[hash]
write at 0x0:xor:CF012886
```

---
