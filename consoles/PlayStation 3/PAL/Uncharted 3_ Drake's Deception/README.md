# Uncharted 3_ Drake's Deception

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES01176  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [end]:read(EOF-3, 4)
set range:0x000008,[end]+7
DECRYPT blowfish_ecb(\
```

---

### Unlock Crushing Difficulty
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_P\\USR-DATA

```
20000A80 00000001
```

---

### Unlock All Chapters
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
42000B20 00000000
42230020 00000000
```

---

### Start With Max Ammo For Left Weapon(you Must Have A Weapon Equipped To Use This Cheat.)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
20005130 000003E7
```

---

### Start With Max Ammo For Right Weapon(you Must Have A Weapon Equipped To Use This Cheat.)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
20005138 000003E7
```

---

### Start With Max Grenades(you Must Have A Weapon Equipped To Use This Cheat.)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
20005140 00000009
```

---

### Update Crc32 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
set [block_length]:read(0x58C,4)
set [block_length]:[block_length]+0x587
set range:0x58C,[block_length]
set [hash]:crc32
write at 0x588:[hash]
```

---

### Update Hmac Sha1 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
set pointer:EOF-0x1F
set range:0x000008,pointer
set [hash]:hmac_sha1(\
set pointer:EOF-0x1F
write next (0):[hash]
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: BCES01176_NDI_UNCHARTED3_BT_*\\USR-DATA

```
set [end]:read(EOF-3, 4)
set range:0x000008,[end]+7
ENCRYPT blowfish_ecb(\
```

---
