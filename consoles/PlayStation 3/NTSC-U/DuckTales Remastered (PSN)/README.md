# DuckTales Remastered (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31126  
**Cheat Type:** Save Editor  
**Source:** [From Azagthoth (CMP)](From Azagthoth (CMP))  

---

## Cheats

### Max Cash
**Author:**   
**Notes:** File: SAVE.DAT

```
200000D0 05F5E0FF
```

---

### 99 Lives On Hard You Must First Kill The 1st Boss For Patch To Work
**Author:**   
**Notes:** File: SAVE.DAT

```
20000019 02620000
```

---

### 9 Hards
**Author:**   
**Notes:** File: SAVE.DAT

```
2000001B 09020000
```

---

### Change The Dificulty Easy
**Author:**   
**Notes:** File: SAVE.DAT

```
20000016 00010000
```

---

### Change The Dificulty Normal
**Author:**   
**Notes:** File: SAVE.DAT

```
20000016 00010001
```

---

### Change The Dificulty Hard
**Author:**   
**Notes:** File: SAVE.DAT

```
20000016 00010002
```

---

### Change The Dificulty Extreme
**Author:**   
**Notes:** File: SAVE.DAT

```
20000016 00010003
```

---

### Update Checksum For Save.dat (required)
**Author:**   
**Notes:** File: SAVE.DAT

```
set pointer:eof+1
set range:0x10,pointer
set [hash]:lookup3_little2(0x04D2, 0x162E)
write at 0x0000:[hash]
```

---
