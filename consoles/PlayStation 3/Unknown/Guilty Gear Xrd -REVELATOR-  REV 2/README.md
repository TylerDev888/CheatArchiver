# Guilty Gear Xrd -REVELATOR-  REV 2

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10329  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Max W$ Money
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
2000E150 0098967F
```

---

### Unlock Artwork Gallery
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
4100CA40 00000505
40100002 00000000
```

---

### Unlock Movie Gallery
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
4000CAC0 00000005
403B0001 00000000
```

---

### Unlock Voice Gallery
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
4100CB40 00000005
408B0001 00000000
```

---

### Unlock Music Gallery
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
4100CC40 00000505
401C0002 00000000
```

---

### Unlock Character Gallery
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
4100CCC0 00000707
401A0002 00000000
```

---

### Update Crc32 For Sys2nd.dat (required)(by Bucanero)
**Author:**   
**Notes:** [- Revelator 2 -]  File: SYS2ND.DAT

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
