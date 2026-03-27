# Metal Gear Solid 5_ The Phantom Pain

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31491  
**Cheat Type:** AP  
**Source:** [web.save-editor.com](https://web.save-editor.com/bbs/patchcode/ps3/bbs.cgi?list=pickup&num=508#)  

---

## Cheats

### Decrypt Save Data (required)
**Author:**   
**Notes:** File: TPP_GAM*  (*Precautions before use*) (Update to match the version [Version 1.12]) (Being in the air command center [Standing by in the ACC ]) (Save data For both GAM0 and GAM1) (If characters and numbers such as fuel resources and common metals disappear on the resource screen,) (open anoth...

```
set range:0x0000,EOF+1
DECRYPT MGS5_TPP(0x22F9710B)
```

---

### Processed Resources
**Author:**   
**Notes:** File: TPP_GAM*

```
420270EC 000F4240
40050004 00000000
```

---

### Plants
**Author:**   
**Notes:** File: TPP_GAM*

```
42027100 00002EE0
40080004 00000000
```

---

### Raw Resources
**Author:**   
**Notes:** File: TPP_GAM*

```
420271D8 003D0900
40050004 00000000
```

---

### Parasites
**Author:**   
**Notes:** File: TPP_GAM*

```
42027164 00001770
40030004 00000000
```

---

### Various Weapons
**Author:**   
**Notes:** File: TPP_GAM*

```
42027120 0000EA60
400F0004 00000000
42027174 0000EA60
40050004 00000000
```

---

### 700 People
**Author:**   
**Notes:** [Soldier Ability Value Change]  File: TPP_GAM*

```
4001FAEB 0000004E
42BC0004 00000000
```

---

### 1400 People
**Author:**   
**Notes:** [Soldier Ability Value Change]  File: TPP_GAM*

```
4001FAEB 0000004E
45780004 00000000
```

---

### 2100 People
**Author:**   
**Notes:** [Soldier Ability Value Change]  File: TPP_GAM*

```
4001FAEB 0000004E
48340004 00000000
```

---

### 2800 People
**Author:**   
**Notes:** [Soldier Ability Value Change]  File: TPP_GAM*

```
4001FAEB 0000004E
4AF00004 00000000
```

---

### 3500 People
**Author:**   
**Notes:** [Soldier Ability Value Change]  File: TPP_GAM*

```
4001FAEB 0000004E
4DAC0004 00000000
```

---

### Update Md5 Checksum (required)
**Author:**   
**Notes:** [\\]  File: TPP_GAM*

```
set range:0x0010,EOF+1
set [hash]:MD5
write at 0x0000:[hash]
```

---

### Encrypt Save Data (required)
**Author:**   
**Notes:** [\\]  File: TPP_GAM*

```
set range:0x0000,EOF+1
ENCRYPT MGS5_TPP(0x22F9710B)
```

---
