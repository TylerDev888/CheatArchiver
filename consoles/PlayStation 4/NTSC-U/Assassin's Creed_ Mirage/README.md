# Assassin's Creed_ Mirage

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA33151  
**Cheat Type:** SaveWizard  

---

## Cheats

### Item Swap
**Author:**   
**Notes:** File: (Manual|Auto|Quick)Save[0-9]+\\(Manual|Auto|Quick)Save[0-9]+.sav

```
80010026 1C000B01
[Main<Item Replacing>]
16000000 B8D11793
B8D11793 00001C00
0B01[Secondary<Item Replacing>]
A8000004 00000008
[Main<Item Want>]
A800001E 00000008
[Secondary]
```

---

### Item Amount
**Author:**   
**Notes:** File: (Manual|Auto|Quick)Save[0-9]+\\(Manual|Auto|Quick)Save[0-9]+.sav

```
80010026 1C000B01
[Main<Main ID of Item>]
16000000 B8D11793
B8D11793 00001C00
0B01[Secondary<Secondary ID of Item>]
8801000D 60748566
00000000 00000700
0B000000 00000000
2800000D [Amount:0000270F:HEX:BIG<Quantity>]
```

---

### Skill Points
**Author:**   
**Notes:** File: (Manual|Auto|Quick)Save[0-9]+\\(Manual|Auto|Quick)Save[0-9]+.sav

```
80010004 C80A5A6E
2800000D 000000[Amount:3D:HEX:BIG]
80020004 C80A5A6E
2800000D 000000[Amount:3D:HEX:BIG]
80030004 C80A5A6E
2800000D 000000[Amount:3D:HEX:BIG]
```

---
