# Borderlands_ The Pre-Sequel

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31445  
**Cheat Type:** Save Editor  
**Source:** [from shaka and chaoszage](from shaka and chaoszage)  

---

## Cheats

### Decompress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Decompress(0x00000018, 15)
```

---

### Max Badass Token
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
80010004 00008A01
28000004 0098967F
```

---

### +500% All Badass Bonus
**Author:**   
**Notes:** File: ~extracted\\00000018.dat

```
80010004 00008A01
2800001D 5A53504D
28000021 45324D37
28000025 564A5439
28000029 50594342
2800002D 41373954
28000031 4B443958
28000035 34384650
28000039 354E4B43
2800003D 5853504D
28000041 45324D37
28000045 564A5439
28000049 47594342
2800004D 41373954
28000051 4B443958
28000055 34394650
28000059 354E4B38
2800005D 5853504D
28000061 45324D37
28000065 564A5439
28000069 4A594342
2800006D 41373154
28000071 4B443958
28000075 34423700
```

---

### Compress Payload (required)
**Author:**   
**Notes:** File: PAYLOAD

```
Compress(0x00000018)
```

---

### Update Sha1 For Payload (required)
**Author:**   
**Notes:** File: PAYLOAD  (set range:0x000014,0x000166)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---

### Update Sha1 For Save0001.sav (required)
**Author:**   
**Notes:** File: SAVE0001.SAV  (set range:0x000014,0x00210F)

```
set pointer:eof+1
set range:0x000014,pointer
set [hash]:SHA1
write at 0x000000:[hash]
```

---
