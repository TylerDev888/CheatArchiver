# Atelier Rorona_ The Alchemist Of Arland DX

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA14023  
**Cheat Type:** SaveWizard  

---

## Cheats

### Set Container Quality To 2000
**Author:** Lotus  
**Notes:** [ITEMS]  File: GAMEDATA[0-9]{2}\\USR-DATA.dat

```
80010008 07000000
D0890100 00000000
92000000 000012C8
4A000008 42F00000
47CF0030 00000000
```

---

### Set Basket Quality to 100 All Items
**Author:** Lotus  
**Notes:** [ITEMS]  File: GAMEDATA[0-9]{2}\\USR-DATA.dat

```
80010008 07000000
D0890100 00000000
92000000 00000008
4A000008 42F00000
40630030 00000000
```

---

### Add Items to Basket/Container{SET To NONE For Traits\\Effects if you dont want any)
**Author:** Lotus  
**Notes:** [ITEMS]  File: GAMEDATA[0-9]{2}\\USR-DATA.dat

```
80010008 07000000
D0890100 00000000
92000000 [TYPE]
28000000 00000895
28000004 0000[IIII<*ITEMID>]
28000008 [AMOUNT:3E80000:FLOAT:BIG<Quality>]
2800000C [TTTT<*Traits1>]
28000010 [TTTT<*Traits2>]
28000014 [TTTT<*Traits3>]
28000018 [TTTT<*Traits4>]
2800001C [TTTT<*Traits5>]
28000020 [EEEE<*Effects1>]
28000024 [EEEE<*Effects2>]
28000028 [EEEE<*Effects3>]
0800002C [AMOUNT:FFFFFFFF:HEX:BIG]
```

---
