# DYNASTY WARRIORS 8_ Xtreme Legends

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** NPJB00510  
**Cheat Type:** Save Editor  

---

## Cheats

### Decrypt App.bin (required)
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
set pointer:eof-1
set range:0x0000,pointer
DECRYPT dw8xl
```

---

### 65535 Gems
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
10001D43 0000FFFF
```

---

### All Generals Max Exp
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
42007FE4 002C7905
40520048 00000000
```

---

### All Generals Attack/defense/physical Strength Max
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
42007FD5 DC05DC05
40520048 00000000
41007FD9 0000E803
40520048 00000000
```

---

### All Generals Aptitude 4-stars
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
42007FDB 64646464
40520048 00000000
```

---

### All Weapon Atributes Lv.10
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4200E721 0A0A0A0A
47260018 00000000
4100E725 00000A0A
47260018 00000000
```

---

### Max Gold
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
20000105 7F969800
```

---

### Facility Materials/weapons Materials Max
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
2001F6D1 0F270F27
```

---

### All Bonds Max
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
41009BF1 00006363
4346000C 00000000
```

---

### All Guards Battle Skill Lv.9
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
40009BE9 00000009
4346000C 00000000
```

---

### All Support Beasts Movement Speed 400
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4101DF11 00009001
40460018 00000000
```

---

### All Weapon Attack Power 255
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN  (Zero4ph)

```
4000E71A 000000FF
47260018 00000000
```

---

### All Weapon Attributes Slots Attribute
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4200E71B 03070C14
47260018 00000000
4100E71F 00001521
47260018 00000000
```

---

### Beast Breakthrough Power Max
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4101DF17 000003E8
40460018 00000000
```

---

### Beast 3 Skills
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4101DF1D 0A0B0C0D
40460018 00000000
```

---

### Breakthrough Power Max
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4101DF17 0000FFFF
40460018 00000000
```

---

### All Abilities Skill Lv.20
**Author:**   
**Notes:** File: SAVEDATA\\APP.BIN

```
4100C63D 00000114
40120002 00000000
```

---

### Rampage 1st Place Score Mod (just Win For Trophy)
**Author:**   
**Notes:** [Challenge Mode Codes]  File: SAVEDATA\\APP.BIN

```
1001FF2D 00000000
```

---

### Bridge Melee 1st Place Score Mod (just Win For Trophy)
**Author:**   
**Notes:** [Challenge Mode Codes]  File: SAVEDATA\\APP.BIN

```
100200BD 00000000
```

---

### Speed Run 1st Place Time Mod (just Win For Trophy)
**Author:**   
**Notes:** [Challenge Mode Codes]  File: SAVEDATA\\APP.BIN

```
1002024D 0000FFFF
```

---

### Arena 1st Place Score Mod (just Win For Trophy)
**Author:**   
**Notes:** [Challenge Mode Codes]  File: SAVEDATA\\APP.BIN

```
100203DD 00000000
```

---

### Inferno Times 1st Place Score Mod (just Win For Trophy)
**Author:**   
**Notes:** [Challenge Mode Codes]  File: SAVEDATA\\APP.BIN

```
1002056D 0000FFFF
```

---

### Update Add For App.bin (required)
**Author:**   
**Notes:** [Encrypt Data]  File: SAVEDATA\\APP.BIN

```
set pointer:eof-1
set [csum]:add(0x0000,pointer)
set [csum]:right([csum],1)
write next (1):[csum]
```

---

### Encrypt App.bin (required)
**Author:**   
**Notes:** [Encrypt Data]  File: SAVEDATA\\APP.BIN

```
set pointer:eof-1
set range:0x0000,pointer
ENCRYPT dw8xl
```

---
