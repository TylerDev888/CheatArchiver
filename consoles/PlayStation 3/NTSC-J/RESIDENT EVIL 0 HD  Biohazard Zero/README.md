# RESIDENT EVIL 0 HD  Biohazard Zero

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** NPJB00726  
**Cheat Type:** Save Editor  

---

## Cheats

### Decrypt Data0.dat (required)
**Author:**   
**Notes:** File: DATA0.DAT

```
set range:0x000000,eof+1
DECRYPT blowfish_ecb(\
```

---

### Save Count 0 Times
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001C90D 00000000
0001C923 00000000
```

---

### Play Time 00:00:00
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
2001C924 00000000
```

---

### Max Hp Rebecca
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DA17 000000FF
```

---

### Max Hp Billy
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DB2B 000000FF
```

---

### Rebecca Physical Strength Maximum (easy)(http://web.save-editor.com/cache/bbs_savedata_ps3/11947.html)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DB87 00000096
```

---

### Rebecca Physical Strength Maximum (normal)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DA17 00000096
```

---

### Rebecca Physical Strength Maximum (hard)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001D95F 00000096
```

---

### Rebecca Item 1: Custom Handgun(http://emu.web-g-p.com/info/system/save_ps3_system_title_decrypt_biohazard_0.html)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
00039097 00000013
1003909A 0000000F
```

---

### Rebecca Item 2: Magnum
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0003909F 0000000A
100390A2 0000000F
```

---

### Rebecca Item 3: Rocket Launcher (infinite)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390A7 00000017
100390AA 0000FFFF
```

---

### Rebecca Item 4: 9999 First Aid Spray
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390AF 00000035
100390B2 0000270F
```

---

### Rebecca Item 5: 9999 Mixed Herbs (full Recovery + Detoxification)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390B7 00000033
100390BA 0000270F
```

---

### Rebecca Item 6: 9999 Ink Ribbons
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390BF 00000037
100390C2 0000270F
```

---

### Billy Maximum Health (easy)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DC9B 000000FA
```

---

### Billy Maximum Health (normal)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DB2B 000000FA
```

---

### Billy Maximum Health (hard)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
0001DA73 000000FA
```

---

### Billy's Item 1: Custom Handgun
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390D3 00000011
100390D6 0000000F
```

---

### Billy's Item 2: Magnum
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390DB 0000000A
100390DE 0000000F
```

---

### Billy's Item 3: Rocket Launcher (infinite)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390E3 00000017
100390E6 0000000F
```

---

### Billy's Item 4: 9999 First Aid Spray
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390EB 00000035
100390EE 0000270F
```

---

### Billy's Item 5: 9999 Mixed Herbs (full Recovery + Detoxification)
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390F3 00000033
100390F6 0000270F
```

---

### Billy's Item 6: 9999 Ink Ribbons
**Author:**   
**Notes:** [Save Slot 1]  File: DATA0.DAT

```
000390FB 00000037
100390FE 0000270F
```

---

### Update Sha1 For Data0.dat (required)
**Author:**   
**Notes:** File: DATA0.DAT

```
set pointer:eof+1
set range:0x000040,pointer
set [hash]:SHA1
write at 0x00000C:[hash]
```

---

### Encrypt Data0.dat (required)
**Author:**   
**Notes:** File: DATA0.DAT

```
set range:0x000000,eof+1
ENCRYPT blowfish_ecb(\
```

---
