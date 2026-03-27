# Monster Hunter Stories 2

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA41231  
**Cheat Type:** SaveWizard  

---

## Cheats

### Edit Item Amount
**Author:**   
**Notes:** File: mhs_slot_([0-9]+|auto)\\.sav

```
[Item]
```

---

### Max Money 9999999
**Author:**   
**Notes:** File: mhs_slot_([0-9]+|auto)\\.sav

```
2000048 0098967F
```

---

### Monster ID
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0x034:0x[ID]
```

---

### Monster Exp
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0x0BC:0x[AMOUNT:7F969800:HEX:LITTLE<Exp>]
```

---

### Monster Level
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0x056:0x[AMOUNT:63:HEX:LITTLE<Level>]
```

---

### Monster Bonus
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0xA8:0x[AMOUNT:63:HEX:BIG<HP>]
write next 0xA9:0x[AMOUNT:63:HEX:BIG<Normal Attack>]
write next 0xAA:0x[AMOUNT:63:HEX:BIG<Fire Attack>]
write next 0xAB:0x[AMOUNT:63:HEX:BIG<Water Attack>]
write next 0xAC:0x[AMOUNT:63:HEX:BIG<Thunder Attack>]
write next 0xAD:0x[AMOUNT:63:HEX:BIG<Ice Attack>]
write next 0xAE:0x[AMOUNT:63:HEX:BIG<Dragon Attack>]
write next 0xAF:0x[AMOUNT:63:HEX:BIG<Normal Defence>]
write next 0xB0:0x[AMOUNT:63:HEX:BIG<Fire Defence>]
write next 0xB1:0x[AMOUNT:63:HEX:BIG<Water Defence>]
write next 0xB2:0x[AMOUNT:63:HEX:BIG<Thunder Defence>]
write next 0xB3:0x[AMOUNT:63:HEX:BIG<Ice Defence>]
write next 0xB4:0x[AMOUNT:63:HEX:BIG<Dragon Defence>]
```

---

### Monster Genes
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0x14C:0x[Gene<Top Left>]
write next 0x150:0x[Gene<Top Centre>]
write next 0x154:0x[Gene<Top Right>]
write next 0x158:0x[Gene<Middle Left>]
write next 0x15C:0x[Gene<Middle Centre>]
write next 0x160:0x[Gene<Middle Right>]
write next 0x164:0x[Gene<Bottom Left>]
write next 0x168:0x[Gene<Bottom Centre>]
write next 0x16C:0x[Gene<Bottom Right>]
```

---

### Monster Riding Action
**Author:**   
**Notes:** [Mod Monster]  File: mhs_slot_([0-9]+|auto)\\.sav

```
search \
write next 0x178:0x[Action<Action 1>]
write next 0x17A:0x[Action<Action 2>]
write next 0x17C:0x[Action<Action 3>]
```

---
