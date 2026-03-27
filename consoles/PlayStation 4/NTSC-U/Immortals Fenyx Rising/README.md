# Immortals Fenyx Rising

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA16345  
**Cheat Type:** SaveWizard  
**Source:** [Mhallice#1926, Skiller#4741](Mhallice#1926, Skiller#4741)  

---

## Cheats

### Item Amount Mod
**Author:**   
**Notes:** File: (DLC[1-2])?(NewGamePlus|DungeonEntrance|Typhon|Quick|Auto|Manual)Save[0-9]{2}\\.sav

```
80010010 0012000B
[Item]
15000000 00000000
280001F3 [AMOUNT:05F5E0FF:HEX:BIG]
```

---

### Item Replacement
**Author:**   
**Notes:** File: (DLC[1-2])?(NewGamePlus|DungeonEntrance|Typhon|Quick|Auto|Manual)Save[0-9]{2}\\.sav

```
80010010 0012000B
[Item<Item You Have>]15000000 00000000
A8000004 00000008
[Item<Item You Want>]
```

---

### Mastery Level 60
**Author:**   
**Notes:** File: (DLC[1-2])?(NewGamePlus|DungeonEntrance|Typhon|Quick|Auto|Manual)Save[0-9]{2}\\.sav

```
80010010 0012000B
[Mastery]
15000000 00000000
28000064 0000003D
```

---

### Mastery Bar Max
**Author:**   
**Notes:** File: (DLC[1-2])?(NewGamePlus|DungeonEntrance|Typhon|Quick|Auto|Manual)Save[0-9]{2}\\.sav

```
8001000E 15000000
CCF70EBE AB7590C6
00000000 00000000
88010011 11000000
[MasteryBar] 00000000
00000700 0B000000
28000011 00000007
```

---
