# The Evil Within

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01916  
**Cheat Type:** Save Editor  

---

## Cheats

### Upgrade Points 999999 (green Gel)
**Author:**   
**Notes:** File: _PLAYER

```
search 0x7A7765692F706C617965722F757067726164655F6974656D
write next (24):0x000F423F
```

---

### Ordinary Keys 45
**Author:**   
**Notes:** File: _PLAYER

```
search 0x73617665726F6F6D5F6B65792F64656661756C74
write next (20):0x0000002D
```

---

### Max Out Abilities
**Author:**   
**Notes:** File: _PLAYER

```
search 0x93688362:10
write next (167):0x00000005
write next (171):0x00000006
write next (175):0x00000005
write next (179):0x00000005
write next (183):0x00000005
write next (187):0x00000005
write next (191):0x00000005
write next (195):0x00000005
write next (199):0x00000005
write next (203):0x00000003
write next (207):0x00000005
write next (211):0x00000005
write next (215):0x00000005
write next (219):0x00000005
write next (223):0x00000005
write next (227):0x00000005
write next (231):0x00000005
```

---

### Max Health
**Author:**   
**Notes:** [Health (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (159):0x434800004348
```

---

### Infinite Health
**Author:**   
**Notes:** [Health (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (159):0x636300006363
```

---

### Reset Time To 0:00
**Author:**   
**Notes:** [Total time played (Choose one)]  File: _PLAYER

```
search 0xDA610A5C:3
write next (-248):0x000000
```

---

### Time Played Is 1 Hour
**Author:**   
**Notes:** [Total time played (Choose one)]  File: _PLAYER

```
search 0xDA610A5C:3
write next (-248):0x000E10
```

---

### Casual
**Author:**   
**Notes:** [Change difficulty to (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (11):0x00
```

---

### Survival
**Author:**   
**Notes:** [Change difficulty to (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (11):0x01
```

---

### Nightmare
**Author:**   
**Notes:** [Change difficulty to (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (11):0x02
```

---

### Akumu
**Author:**   
**Notes:** [Change difficulty to (Choose one)]  File: _PLAYER

```
search 0x93688362:10
write next (11):0x03
```

---

### Experimental (some Enemies Already Dead)
**Author:**   
**Notes:** [Change difficulty to (Choose one)]  File: _PLAYER  (maybe only has effect on QUICKSAVE) (might get stuck if the story depends on killing an enemy to) (open a door to get further)

```
search 0x93688362:10
write next (11):0x04
```

---

### Syringes 99
**Author:**   
**Notes:** [Max out items]  File: _PLAYER

```
search 0x66697273746169642F737972696E6765
write next (16):0x00000063
write next (24):0x00000063
```

---

### Med Kits 99
**Author:**   
**Notes:** [Max out items]  File: _PLAYER

```
search 0x66697273746169642F6D65646963616C5F6B6974
write next (20):0x00000063
```

---

### Matchsticks 99
**Author:**   
**Notes:** [Max out items]  File: _PLAYER

```
search 0x7A7765692F706C617965722F6D61746368737469636B
write next (22):0x00000063
write next (30):0x00000063
```

---

### Trap Parts 999
**Author:**   
**Notes:** [Max out items]  File: _PLAYER

```
search 0x7A7765692F706C617965722F747261705F7061727473
write next (22):0x000003E7
```

---

### Grenades 999
**Author:**   
**Notes:** [Max out items]  File: _PLAYER

```
search 0x7A7765692F7468726F7761626C652F6772656E6164652F6D3234
write next (26):0x000003E7
write next (34):0x000003E7
```

---

### Replace Handgun With Magnum
**Author:**   
**Notes:** [Replace Handgun with Magnum *]  File: _PLAYER

```
search 0x776561706F6E2F706973746F6C00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F706973746F6C2F7374616E64617264
write next (0):0x776561706F6E2F6D61676E756D00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F6D61676E756D2F7374616E64617264
```

---

### Replace Handgun Ammo Stock With Magnum Ammo Stock
**Author:**   
**Notes:** [Replace Handgun with Magnum *]  File: _PLAYER

```
search 0x616D6D6F2F706973746F6C2F7374616E64617264
write next (0):0x616D6D6F2F6D61676E756D2F7374616E64617264
search 0x616D6D6F2F706973746F6C2F7374616E64617264:2
write next (0):0x616D6D6F2F6D61676E756D2F7374616E64617264
```

---

### Change Magnum Back To Handgun
**Author:**   
**Notes:** [Change Magnum back to Handgun * (chp.6)]  File: _PLAYER

```
search 0x776561706F6E2F6D61676E756D00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F6D61676E756D2F7374616E64617264
write next (0):0x776561706F6E2F706973746F6C00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F706973746F6C2F7374616E64617264
```

---

### Change Magnum Ammo Stock Back To Handgun Ammo Stock
**Author:**   
**Notes:** [Change Magnum back to Handgun * (chp.6)]  File: _PLAYER

```
search 0x616D6D6F2F6D61676E756D2F7374616E64617264
write next (0):0x616D6D6F2F706973746F6C2F7374616E64617264
search 0x616D6D6F2F6D61676E756D2F7374616E64617264:2
write next (0):0x616D6D6F2F706973746F6C2F7374616E64617264
```

---

### Handgun Max Clip + 9999
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F706973746F6C00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F706973746F6C2F7374616E64617264
write next (49):0x0000270F
search 0x616D6D6F2F706973746F6C2F7374616E64617264:2
write next (20):0x0000270F
write next (28):0x0000270F
```

---

### Rifle Max Clip + 9999
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F7269666C6500000001FFFFFFFFFFFFFFFF13000000616D6D6F2F7269666C652F7374616E64617264
write next (47):0x0000270F
search 0x616D6D6F2F7269666C652F7374616E64617264:2
write next (19):0x0000270F
write next (27):0x0000270F
```

---

### Magnum Max Clip + 9999
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F6D61676E756D00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F6D61676E756D2F7374616E64617264
write next (49):0x0000270F
search 0x616D6D6F2F6D61676E756D2F7374616E64617264:2
write next (20):0x0000270F
write next (28):0x0000270F
```

---

### Machinegun Max Clip + 9999
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F6D616368696E6567756E00000001FFFFFFFFFFFFFFFF18000000616D6D6F2F6D616368696E6567756E2F7374616E64617264
write next (57):0x0000270F
search 0x616D6D6F2F6D616368696E6567756E2F7374616E64617264:2
write next (24):0x0000270F
write next (32):0x0000270F
```

---

### Rocketlauncher Max Clip + 999
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F726F636B65746C61756E6368657200000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F726F636B65746C61756E636865722F7374616E64617264
write next (65):0x000003E7
search 0x616D6D6F2F726F636B65746C61756E636865722F7374616E64617264:2
write next (28):0x000003E7
write next (36):0x000003E7
```

---

### Rocketlauncher Ammo 99 (final Boss)
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F726F636B65746C61756E636865725F6C61737400000001FFFFFFFFFFFFFFFF1E000000616D6D6F2F726F636B65746C61756E636865722F666F725F616C70686133
write next (72):0x00000063
search 0x616D6D6F2F726F636B65746C61756E636865722F666F725F616C70686133:2
write next (30):0x00000063
write next (38):0x00000063
```

---

### Burst Handgun Max Clip
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F62757273745F68616E6467756E00000001FFFFFFFFFFFFFFFF14000000616D6D6F2F706973746F6C2F7374616E64617264
write next (56):0x0000270F
```

---

### High Penetrating Sniper Rifle Max Clip
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F70656E6574726174696E675F7269666C6500000001FFFFFFFFFFFFFFFF13000000616D6D6F2F7269666C652F7374616E64617264
write next (59):0x0000270F
```

---

### Shotgun Max Clip + 9999, Look Below For Alt.code** Dont Use Both Codes
**Author:**   
**Notes:** [Max clip ammo + stock]  File: _PLAYER

```
search 0x776561706F6E2F726567696D6573686F7467756E00000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164
write next (64):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:2
write next (28):0x0000270F
write next (36):0x0000270F
```

---

### Normal Shotgun, Only Use If You Dont Have The Double B.shotgun
**Author:**   
**Notes:** [Shotgun max clip + 9999 (Choose one) ONLY **]  File: _PLAYER

```
search 0x776561706F6E2F726567696D6573686F7467756E00000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164
write next (64):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:2
write next (28):0x0000270F
write next (36):0x0000270F
```

---

### Double B.shotgun, Only Use If You Dont Have Picked Up Normal
**Author:**   
**Notes:** [Shotgun max clip + 9999 (Choose one) ONLY **]  File: _PLAYER

```
search 0x776561706F6E2F646F75626C6562617272656C5F73686F7467756E00000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F73686F7467756E2F6275636B7368 6F745F737072656164
write next (143):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:2
write next (28):0x0000270F
write next (36):0x0000270F
```

---

### Normal And Double B.shotgun, Only Use If You Have Both Shotguns
**Author:**   
**Notes:** [Shotgun max clip + 9999 (Choose one) ONLY **]  File: _PLAYER

```
search 0x776561706F6E2F726567696D6573686F7467756E00000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164
write next (64):0x0000270F
search 0x776561706F6E2F646F75626C6562617272656C5F73686F7467756E00000001FFFFFFFFFFFFFFFF1C000000616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164
write next (143):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:3
write next (28):0x0000270F
write next (36):0x0000270F
```

---

### Handgun(s) Max Clip + 9999
**Author:**   
**Notes:** [Alternative weapon codes (if others dont work)]  File: _PLAYER

```
search 0x616D6D6F2F706973746F6C2F7374616E64617264
write next (20):0x0000270F
write next (28):0x0000270F
search 0x616D6D6F2F706973746F6C2F7374616E64617264:2
write next (20):0x0000270F
write next (28):0x0000270F
search 0x616D6D6F2F706973746F6C2F7374616E64617264:3
write next (20):0x0000270F
write next (28):0x0000270F
search 0x616D6D6F2F706973746F6C2F7374616E64617264:4
write next (20):0x0000270F
write next (28):0x0000270F
```

---

### Shotgun(s) Max Clip + 9999
**Author:**   
**Notes:** [Alternative weapon codes (if others dont work)]  File: _PLAYER

```
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164
write next (28):0x0000270F
write next (36):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:2
write next (28):0x0000270F
write next (36):0x0000270F
search 0x616D6D6F2F73686F7467756E2F6275636B73686F745F737072656164:3
write next (28):0x0000270F
write next (36):0x0000270F
```

---

### Rifle(s) Max Clip + 9999
**Author:**   
**Notes:** [Alternative weapon codes (if others dont work)]  File: _PLAYER

```
search 0x616D6D6F2F7269666C652F7374616E64617264
write next (19):0x0000270F
write next (27):0x0000270F
search 0x616D6D6F2F7269666C652F7374616E64617264:2
write next (19):0x0000270F
write next (27):0x0000270F
search 0x616D6D6F2F7269666C652F7374616E64617264:3
write next (19):0x0000270F
write next (27):0x0000270F
search 0x616D6D6F2F7269666C652F7374616E64617264:4
write next (19):0x0000270F
write next (27):0x0000270F
```

---

### Explosive Bolts(you Need At Least One Of Each Stock Item To Be Able To Max Them Out And Overload Values)
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F626F6D62
write next (18):0x00000063
write next (26):0x00000063
search 0x616D6D6F2F747261705F67756E2F626F6D62:2
write next (18):0x00000063
write next (26):0x00000063
```

---

### Shock Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F7465736C61
write next (19):0x00000063
write next (27):0x00000063
search 0x616D6D6F2F747261705F67756E2F7465736C61:2
write next (19):0x00000063
write next (27):0x00000063
```

---

### Flash Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F666C617368
write next (19):0x00000063
write next (27):0x00000063
search 0x616D6D6F2F747261705F67756E2F666C617368:2
write next (19):0x00000063
write next (27):0x00000063
```

---

### Freeze Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F667265657A65
write next (20):0x00000063
write next (28):0x00000063
search 0x616D6D6F2F747261705F67756E2F667265657A65:2
write next (20):0x00000063
write next (28):0x00000063
```

---

### Harpoon Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F686172706F6F6E
write next (21):0x00000063
write next (29):0x00000063
search 0x616D6D6F2F747261705F67756E2F686172706F6F6E:2
write next (21):0x00000063
write next (29):0x00000063
```

---

### Fire Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F66697265
write next (18):0x00000063
write next (26):0x00000063
search 0x616D6D6F2F747261705F67756E2F66697265:2
write next (18):0x00000063
write next (26):0x00000063
```

---

### Poison Bolts
**Author:**   
**Notes:** [Agony Crossbow ammo 99]  File: _PLAYER

```
search 0x616D6D6F2F747261705F67756E2F706F69736F6E
write next (20):0x00000063
write next (28):0x00000063
search 0x616D6D6F2F747261705F67756E2F706F69736F6E:2
write next (20):0x00000063
write next (28):0x00000063
```

---

### Update Md5_xor For _player (required)
**Author:**   
**Notes:** File: _PLAYER  (set range:0x000000,0x01FFFB) (write at 0x01FFFC:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---

### Update Md5_xor For _details (required)
**Author:**   
**Notes:** File: _DETAILS  (set range:0x000000,0x00018F) (write at 0x000190:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---

### Update Md5_xor For _map (required)
**Author:**   
**Notes:** File: _MAP  (set range:0x000000,0x007FFB) (write at 0x007FFC:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---
