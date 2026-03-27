# The Darkness II

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01388  
**Cheat Type:** AP  
**Source:** [From Game Genie For PS3 & Keha World](From Game Genie For PS3 & Keha World)  

---

## Cheats

### Essence 999 *3 Figures Of Current Price
**Author:**   
**Notes:** File: CONTINUE.SAV

```
search 0x54616C656E74506F696E74733D:1
write next D: 393939
```

---

### Essence 9999 *4 Figures Of Current Price
**Author:**   
**Notes:** File: CONTINUE.SAV

```
search 0x54616C656E74506F696E74733D:1
write next D: 39393939
```

---

### Essence 99999 *5 Figures Of Current Price
**Author:**   
**Notes:** File: CONTINUE.SAV

```
search 0x54616C656E74506F696E74733D:1
write next D: 3939393939
```

---

### Unlock New Game+
**Author:**   
**Notes:** File: CONTINUE.SAV

```
8001000C 4861734E
65774761 6D65506C
08000013 00000031
```

---

### Update Md5 In Continue.sav (required)
**Author:**   
**Notes:** File: CONTINUE.SAV  (set range:0x000010,0x0244F7)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:MD5
write at 0x000000:[hash]
```

---

### Update Md5 In Settings (required)
**Author:**   
**Notes:** File: SETTINGS  (set range:0x000010,0x005CA1)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:MD5
write at 0x000000:[hash]
```

---

### Update Md5 Hashes (required)
**Author:**   
**Notes:** File: CONTINUE.SAV

```
set pointer:eof
set range:0x10, pointer+1
set [md5]:md5
write at 0x0:[md5]
```

---
