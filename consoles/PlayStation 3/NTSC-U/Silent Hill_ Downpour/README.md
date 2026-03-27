# Silent Hill_ Downpour

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30565  
**Cheat Type:** Save Editor  
**Source:** [By chaoszage](By chaoszage)  

---

## Cheats

### Super More Health(999)(normal Max Health Is 100)
**Author:**   
**Notes:** File: PAYLOAD

```
search \
search next 0x22
write next 1:\
```

---

### 9 F.a.kits(use This If More Than 1 And Less Than 10)
**Author:**   
**Notes:** [First Aid Kit(choose One)]  File: PAYLOAD

```
search \
write next (-23):0x3939
```

---

### 99 F.a.kits(use This If More Than 10)
**Author:**   
**Notes:** [First Aid Kit(choose One)]  File: PAYLOAD

```
search \
write next (-24):0x3939
```

---

### 9 Handgun Ammo(use This If More Than 1 And Less Than 10)
**Author:**   
**Notes:** [Handgun Ammo(choose One)]  File: PAYLOAD

```
search \
write next (-77):0x3939
```

---

### 99 Handgun Ammo(use This If More Than 10)
**Author:**   
**Notes:** [Handgun Ammo(choose One)]  File: PAYLOAD

```
search \
write next (-78):0x3939
```

---

### 9 Shotgun Ammo(use This If More Than 1 And Less Than 10)
**Author:**   
**Notes:** [Shotgun Ammo(choose One)]  File: PAYLOAD

```
search \
write next (-100):0x3939
```

---

### 99 Shotgun Ammo(use This If More Than 10)
**Author:**   
**Notes:** [Shotgun Ammo(choose One)]  File: PAYLOAD

```
search \
write next (-101):0x3939
```

---

### Easy
**Author:**   
**Notes:** [Game Difficulty(choose One)]  File: PAYLOAD

```
search \
write next 15:\
```

---

### Normal
**Author:**   
**Notes:** [Game Difficulty(choose One)]  File: PAYLOAD

```
search \
write next 15:\
```

---

### Hard
**Author:**   
**Notes:** [Game Difficulty(choose One)]  File: PAYLOAD

```
search \
write next 15:\
```

---

### Update Sha1 Checksum(required)
**Author:**   
**Notes:** File: PAYLOAD

```
write at 0x4:0000000000000000000000000000000000000000
set pointer:eof+1
set range:0x000000,pointer
set [hash]:SHA1
write at 0x000004:[hash]
```

---
