# Hunted_ The Demon's Forge

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS30406  
**Cheat Type:** AP  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Decompress Payload (required)
**Author:**   
**Notes:** File: BLUS30406-PROFILE\\PAYLOAD

```
Decompress(0x00000018, 15)
```

---

### Max Gold
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
20000173 000F423F
```

---

### 189999 Gold
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
80010004 00002301
28000004 0002E62F
```

---

### Compress Payload (required)
**Author:**   
**Notes:** File: BLES01309-PROFILE\\PAYLOAD

```
Compress(0x00000018)
```

---

### Update Sha1 (required)
**Author:**   
**Notes:** File: BLES01309-PROFILE\\PAYLOAD  (set range:0x000014,0x00034C)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
