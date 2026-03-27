# The Last of Us_ Part II

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA17962  
**Cheat Type:** AP  
**Source:** [source: discord](source: discord)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [end]:read(0x08, 4)
set [end]:endian_swap
set range:0x000010,[end]+0x0F
DECRYPT blowfish_ecb(\
```

---

### Inf Silencer (must Have One, Must Use Load Save)
**Author:**   
**Notes:** File: USR-DATA

```
80010010 5A896447
3E303014 00000000
00000000 00000000
28000018 000000FF
80020010 5A896447
3E303014 00000000
00000000 00000000
28000018 000000FF
```

---

### Add Inf Silencer (use If U Dont Have One)-ellie
**Author:**   
**Notes:** File: USR-DATA

```
80010020 861B638E
BAADBCC4 6C30D500
85A901F8 6969B1A2
7EFE1381 11313532
D784E928 00000000
88010024 00000000
00000000 00000000
00000000 00000000
00000000 00000000
00000000 01010101
A8000000 00000008
5A896447 3E303014
A8000010 00000010
01000000 00000000
FF000000 00000000
```

---

### Add Inf Silencer (use If U Dont Have One)-abby
**Author:**   
**Notes:** File: USR-DATA

```
80040020 861B638E
BAADBCC4 6C30D500
85A901F8 6969B1A2
7EFE1381 11313532
D784E928 00000000
88010024 00000000
00000000 00000000
00000000 00000000
00000000 00000000
00000000 01010101
A8000000 00000008
5A896447 3E303014
A8000010 00000010
01000000 00000000
FF000000 00000000
```

---

### All Ellie Character Upgrades (gives Ellie Extra Hp 6 Boxs)
**Author:**   
**Notes:** File: USR-DATA

```
80010010 193DC7D0
9B27D7DE 90414BEC
FF8A50AA 00000000
A8000048 0000000A
FFFFFFFF FFFFFFFF
FFFF0000 00000000
```

---

### Max Points
**Author:**   
**Notes:** File: USR-DATA

```
20001150 00000000
10001AB0 00000207
```

---

### All Concept Art Purchased
**Author:**   
**Notes:** File: USR-DATA

```
20001370 0000003F
20001460 FFFFFFFE
```

---

### All Models Purchased
**Author:**   
**Notes:** File: USR-DATA

```
200012E0 6FB79B3F
20001478 0007DFC1
20001480 FEFF7FFF
```

---

### All Abby Character Upgrades
**Author:**   
**Notes:** File: USR-DATA

```
80020010 193DC7D0
9B27D7DE 90414BEC
FF8A50AA 00000000
A8000048 0000000A
FFFFFFFF FFFFFFFF
FFFF0000 00000000
```

---

### All - Max Melee Durability
**Author:**   
**Notes:** File: USR-DATA  (Advanced codes) (Selective - Max Melee Durability: Must have item before use) (See ID list to fill in X/G) (Ellie - 255) (80010018 F52C8095) (1BF61EB4 9370C643) (C793FDAD CD277F13) (1B4A77C7 00000000) (88010008 XXXXXXXX) (GGGGGGGG 00000000) (28000008 7FFFFFFF) (28000010 7FFFFFFF)...

```
80010010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
80020010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
80030010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
80040010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
80050010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
80060010 F52C8095
1BF61EB4 9370C643
C793FDAD 00000000
28000060 7FFFFFFF
28000068 7FFFFFFF
28000070 00000001
```

---

### Update Crc32-c Checksum For Usr-data (required)(Castagnoli CRC32)
**Author:**   
**Notes:** File: USR-DATA

```
set [block_length]:read(0x594,4)
set [block_length]:endian_swap
set [block_length]:[block_length]+0x58F
set range:0x594,[block_length]
set crc_bandwidth:32
set crc_polynomial:0x1EDC6F41
set crc_initial_value:0xFFFFFFFF
set crc_output_xor:0xFFFFFFFF
set crc_reflection_input:1
set crc_reflection_output:1
set [hash]:crc
set [hash]:endian_swap
write at 0x590:[hash]
```

---

### Update Hmac Sha1 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set pointer:EOF-0x1F
set range:0x000010,pointer
set [hash]:hmac_sha1(\
write next (0):[hash]
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [end]:read(0x08, 4)
set [end]:endian_swap
set range:0x000010,[end]+0x0F
ENCRYPT blowfish_ecb(\
```

---
