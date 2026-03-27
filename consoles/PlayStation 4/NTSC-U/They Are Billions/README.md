# They Are Billions

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA13330  
**Cheat Type:** AP  
**Source:** [source: XxUnkn0wnxX](source: XxUnkn0wnxX)  

---

## Cheats

### Set Resources To Max Cap
**Author:**   
**Notes:** File: *  (Template:) (B0010004 ZZZZZZZZ) (93000000 00000010) (4A000000 XXXXXXXX) (40050004 00000000) (Where Z, Money value) (Where X, Value to set money & all resources) (Possible Values:) (Hex-Dec) (3B9AC9FF = 999999999) (0098967F = 9999999) (000F423F = 999999) (00001388 = 5000) (000003E7 = 999)...

```
B0010004 F00A0000
93000000 00000010
4A000000 0098967F
40050004 00000000
```

---

### Set Command Center Health To 9999999
**Author:**   
**Notes:** File: *

```
80010004 88130000
28000000 0098967F
```

---

### Sets Resources To Max Cap
**Author:** XxUnkn0wnxX  
**Notes:** File: save\\[0-9A-Za-z]{1,16}.zxsav

```
80010017 54726169
6E20746F 20436F6D
6D616E64 2043656E
74657200 00000000
4A0001C0 0098967F
40050004 00000000
```

---

### Template
**Author:** XxUnkn0wnxX  
**Notes:** File: save\\[0-9A-Za-z]{1,16}.zxsav

```
B0010004 [AMOUINT:00000000:HEX:LITTLE<CurrentMoneyAmount>]
93000000 00000010
4A000000 [AMOUINT:00000000:HEX:BIG<ResourcesAmountWanted>]
40050004 00000000
```

---

### Sets Resources To Max Cap - Using Money Value Offset
**Author:** XxUnkn0wnxX  
**Notes:** File: save\\[0-9A-Za-z]{1,16}.zxsav

```
B0010004 F00A0000
93000000 00000010
4A000000 0098967F
40050004 00000000
```

---

### Sets Resources To Max Cap - Survival Only
**Author:** XxUnkn0wnxX  
**Notes:** File: save\\[0-9A-Za-z]{1,16}.zxsav

```
C0020008 0000034A
4A000051 0098967F
40050004 00000000
```

---
