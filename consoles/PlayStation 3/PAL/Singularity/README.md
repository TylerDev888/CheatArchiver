# Singularity

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00560  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### E99 Tech
**Author:**   
**Notes:** File: BLES00560-PROFILE\\PAYLOAD

```
80010006 02000000
C5010000 00000000
28000006 0098967F
```

---

### Max Health Packs
**Author:**   
**Notes:** File: BLES00560-PROFILE\\PAYLOAD

```
80010006 02000000
C2010000 00000000
28000006 00000005
```

---

### Ar9 Valkyrie
**Author:**   
**Notes:** [Max Ammo]  File: BLES00560-PROFILE\\PAYLOAD

```
80010006 02000000
8C010000 00000000
28000006 0098967F
```

---

### Volk S4
**Author:**   
**Notes:** [Max Ammo]  File: BLES00560-PROFILE\\PAYLOAD

```
80010006 02000000
8D010000 00000000
28000006 0098967F
```

---

### Centurion
**Author:**   
**Notes:** [Max Ammo]  File: BLES00560-PROFILE\\PAYLOAD

```
80010006 02000000
99010000 00000000
28000006 0098967F
```

---

### Update Sha1 (required)
**Author:**   
**Notes:** File: BLES00560-PROFILE\\PAYLOAD  (set range:0x000014,0x000359)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
