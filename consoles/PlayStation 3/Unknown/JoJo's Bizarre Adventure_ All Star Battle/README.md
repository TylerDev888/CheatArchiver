# JoJo's Bizarre Adventure_ All Star Battle

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10217  
**Cheat Type:** Save Editor  
**Source:** [checksum fixer by chaoszage](checksum fixer by chaoszage)  

---

## Cheats

### Gold 9999900
**Author:**   
**Notes:** File: JOJOASB.S

```
20001CB0 0098961C
```

---

### Gold 99999999 (alt)
**Author:**   
**Notes:** File: JOJOASB.S

```
20001CB0 05F5E0FF
```

---

### Character Unlock - Jean Pierre Polnareff
**Author:**   
**Notes:** File: JOJOASB.S

```
000032DF 00000040
000032E3 00000040
000032E7 00000040
```

---

### Character Unlock - Dio Brando
**Author:**   
**Notes:** File: JOJOASB.S

```
00007557 00000040
0000755B 00000040
0000755F 00000040
```

---

### Character Unlock - Wamuu
**Author:**   
**Notes:** File: JOJOASB.S

```
00008B7F 00000040
00008B83 00000040
00008B87 00000040
```

---

### All Story Scenarios Cleared
**Author:**   
**Notes:** File: JOJOASB.S

```
4016D600 00000004
48000068 00000000
```

---

### All Legend Missions Cleared
**Author:**   
**Notes:** File: JOJOASB.S

```
4116D608 00000404
48000068 00000000
4016D60A 00000004
48000068 00000000
```

---

### All Characters Unlocked
**Author:**   
**Notes:** File: JOJOASB.S

```
40001CB7 00000040
40801628 00000000
40001CBB 00000040
40801628 00000000
40001CBF 00000040
40801628 00000000
```

---

### Money
**Author:**   
**Notes:** File: JOJOASB.S

```
write at 0x00001CB1:0xFFFF
```

---

### Update Crc32big For Jojoasb.s (required)
**Author:**   
**Notes:** File: JOJOASB.S  (set range:0x000000,0x2038F3) (write at 0x2038F4:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32Big
set pointer:eof-3
write next (0):[hash]
```

---
