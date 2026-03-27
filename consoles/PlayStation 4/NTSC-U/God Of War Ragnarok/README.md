# God Of War Ragnarok

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA34384  
**Cheat Type:** SaveWizard  

---

## Cheats

### Item Replace
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
80010008 [Item<Item you Have>] 00000000
A8000000 00000008
[Item<Item You Want>]
```

---

### Item Quantity
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
80010008 [Item] 00000000
28000008 [AMOUNT:05F5E0FF:HEX:BIG<Quantity>]
```

---

### Item Replace and Quantity (Can use this to move Things from Base Game to DLC to)
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
80010008 [Item<Item you Have>] 00000000
A8000000 00000008
[Item<Item You Want>]
28000008 [AMOUNT:05F5E0FF:HEX:BIG<Quantity>]
```

---

### Increase Dew Stats (Need to have one Dew for code to work)
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
80010008 [Dew] 00000000
28000008 [AMOUNT:05F5E0FF:HEX:BIG<1 Equal 2 so 500 in save is 1000 in game>]
```

---

### Add Item To Blacksmith Chest(Need to have got at least 1 item from it before)
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
80010008 B0BDD5E2
372DB672 00000000
D8000008 03020000
A8000014 0000000C
[Item<Item You Want>]
[AMOUNT:05F5E0FF:HEX:BIG<Quantity>] 00000000
```

---

### Change Difficulty (Re-save to see change) provided by xxunkn0wnxx$0001
**Author:**   
**Notes:** File: GOWRSAVE[0-9]+

```
95000000 0002F440
D8000000 01000002
18000002 0000[Diff]
```

---
