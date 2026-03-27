# Dead Space 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01733  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Health
**Author:**   
**Notes:** File: USR-DATA

```
80010004 25EA8DB7
28000018 43480000
```

---

### Max Statis
**Author:**   
**Notes:** File: USR-DATA

```
80010004 25EA8DB7
2800001C 42A00000
```

---

### Max Air
**Author:**   
**Notes:** File: USR-DATA

```
80010004 25EA8DB7
28000020 43700000
```

---

### Max Armor
**Author:**   
**Notes:** File: USR-DATA

```
80010004 25EA8DB7
28000030 43340000
```

---

### Have All Backpack Slots
**Author:**   
**Notes:** File: USR-DATA

```
80010004 25EA8DB7
2800002C 00000019
```

---

### Tungsten
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
2800001C 000F423F
```

---

### Semiconductor
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
28000020 000F423F
```

---

### Scrap Metal
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
28000024 000F423F
```

---

### Somatic Gel
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
28000028 000F423F
```

---

### Transoucer
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
2800002C 000F423F
```

---

### Ration Seals
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010004 BC2179DD
28000030 000F423F
```

---

### Devil Horns Replaces Your Primary Weapon In Any Mode.
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
80010010 BADBADBA
BEEFBEEF EAC15A55
91100911 00000000
28000010 52CDC428
28000014 9DC149AF
28000018 56315357
2800001C 45435349
28000020 52CDC3DF
28000024 A22E64B1
28000028 56315357
2800002C 45435349
28000030 52CDC3DF
28000034 AC6EDCBF
28000038 56315357
2800003C 45435349
```

---

### Easy Records Trophies:do 1 More Time Of Each Action Gain Particular Trophy(by Chaoszage)
**Author:**   
**Notes:** [Max Resources]  File: USR-DATA

```
search 0x31CC877D413D0C17484C4143304E554F31CC877D5205218F
write next (-320):000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8000003E8
```

---

### Init Sdbm For Hed-data (required)
**Author:**   
**Notes:** [Checksum]  File: HED-DATA

```
set [usr_size]:read(0x4C, 4)
write at 0x08:0x00000000
set range:0x0000,eof+1
set [hash_init]:sdbm
```

---

### Calculate Sdbm For Usr-data (required)
**Author:**   
**Notes:** [Checksum]  File: USR-DATA

```
set [usr_size]:[usr_size]-1
set range:0x0000,[usr_size]
set [hash]:sdbm:[hash_init]
```

---

### Update Sdbm For Hed-data (required)
**Author:**   
**Notes:** [Checksum]  File: HED-DATA

```
write at 0x08:[hash]
```

---
