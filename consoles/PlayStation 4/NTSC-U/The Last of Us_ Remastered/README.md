# The Last of Us_ Remastered

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA00552  
**Cheat Type:** AP  
**Source:** [source:](source:)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA*

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x000008,[end]+7
DECRYPT blowfish_ecb(\
```

---

### Infinite Current Melee Weapon
**Author:**   
**Notes:** File: USR-DATA*

```
10004150 0000FFFF
```

---

### Upgrade Current Melee Weapon
**Author:**   
**Notes:** File: USR-DATA*

```
00004148 00000001
```

---

### Difficulty Levels
**Author:**   
**Notes:** File: USR-DATA*  \\\\28000004 000000xx \\\\28000004 000000xx (xx ??) (01 easy) (02 normal) (03 hard) (04 survivor)

```
80010004 C8DC7F3E
80010004 288D5E5B
```

---

### Grounded Plus Mode
**Author:**   
**Notes:** File: USR-DATA*  (Advanced codes) (Weapons	            Id's) (2x4	              85A11CED) (Pipe	              1DEE1944) (Axe	              BB08ED37) (Machete: 	          8E346d22) (Bat	              783DF18C) (9MM Pistol	          326334FC) (Revolver	          272DACA9) (Diablo	              4156...

```
80010004 C8DC7F3E
28000004 00000005
80010004 96778EBD
28000004 00000001
```

---

### Add Upgraded And Infinite Axe
**Author:**   
**Notes:** File: USR-DATA*

```
A0004134 00000029
BB08ED37 00000000
00000000 00000000
00000075 01000000
03000000 FFFF0000
00000000 00000000
01000000 00000000
```

---

### Add Upgraded And Infinite Bat
**Author:**   
**Notes:** File: USR-DATA*

```
A0004134 00000029
783DF18C 00000000
00000000 00000000
00000075 01000000
03000000 FFFF0000
00000000 00000000
01000000 00000000
```

---

### Add Upgraded And Infinite Machete
**Author:**   
**Notes:** File: USR-DATA*

```
A0004134 00000029
8E346D22 00000000
00000000 00000000
00000075 01000000
03000000 FFFF0000
00000000 00000000
01000000 00000000
```

---

### Add Assault Rifle
**Author:**   
**Notes:** File: USR-DATA*

```
A0003FB4 00000029
64A365D0 1E000000
00000000 00000000
00000074 00000000
00000000 00000000
00000000 00000000
01000000 00000000
```

---

### 65k Ammo And Consumables
**Author:**   
**Notes:** File: USR-DATA*  (Swap Current Melee weapon) (20004134 XXXXXXXX)

```
A00041D8 00000024
FFFFFFFF FFFFFFFF
FFFFFFFF 0000FFFF
FFFFFFFF FFFF0000
FFFFFFFF 0000FFFF
FFFFFFFF 00000000
```

---

### Update Crc32 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA*

```
set [block_length]:read(0x58C,4)
set [block_length]:endian_swap
set [block_length]:[block_length]+0x587
set range:0x58C,[block_length]
set [hash]:crc32
set [hash]:endian_swap
write at 0x588:[hash]
```

---

### Update Hmac Sha1 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA*

```
set pointer:EOF-0x23
set range:0x000008,pointer
set [hash]:hmac_sha1(\
write next (0):[hash]
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA*

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x000008,[end]+7
ENCRYPT blowfish_ecb(\
```

---
