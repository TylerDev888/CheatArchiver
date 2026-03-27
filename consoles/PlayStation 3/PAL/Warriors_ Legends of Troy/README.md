# Warriors_ Legends of Troy

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01183  
**Cheat Type:** Save Editor  
**Source:** [From chaoszage](From chaoszage)  

---

## Cheats

### Max Kleos
**Author:**   
**Notes:** File: PROFILE

```
search 0x420067006D:1
search next 0x290049007400:1
write next (-11):0x05F5E0FF
```

---

### All Stages In All Difficulties Cleared - Game Must Be Completed Once
**Author:**   
**Notes:** File: PROFILE  (Complete any stage in any difficulty will unlock Helen art 3 and All Cheats) (stage 1 Landing) (stage 2 Perimeter) (stage 3 StormFont) (stage 4 Honour) (stage 5 Conquest) (stage 6 Blood) (stage 7 Renown) (stage 8 Plague) (stage 9 Champion) (stage 10 Nightfall) (stage 11 Tide) (sta...

```
search 0x4700300031
write next 1D:0x01010101
search 0x4700300033
write next 1B:0x01010101
search 0x5400300033
write next 1D:0x01010101
search 0x5400300036
write next 15:0x01010101
search 0x4700300035
write next 19:0x01010101
search 0x5400300034
write next 13:0x01010101
search 0x4700300036
write next 15:0x01010101
search 0x4700300037
write next 1B:0x01010101
search 0x5400300038
write next 19:0x01010101
search 0x4700300038
write next 1B:0x01010101
search 0x5400300039
write next 25:0x01010101
search 0x4700300039
write next 1F:0x01010101
search 0x5400310030
write next 19:0x01010101
search 0x4700310030
write next 13:0x01010101
search 0x5400310031
write next 21:0x01010101
search 0x4700310031
write next 13:0x01010101
search 0x5400310034
write next 17:0x01010101
search 0x5400310035
write next 1D:0x01010101
search 0x4700310035
write next 17:0x01010101
search 0x4700310036
write next 17:0x01010101
search 0x5400310036
write next 19:0x01010101
```

---

### Scenario: Update Crc32 (required)
**Author:**   
**Notes:** File: SCENARIO

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next(0):[hash]
```

---

### Profile: Update Crc32 (required)
**Author:**   
**Notes:** File: PROFILE

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next(0):[hash]
```

---

### Settings: Update Crc32 (required)
**Author:**   
**Notes:** File: SETTINGS

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:CRC32
set pointer:eof-3
write next(0):[hash]
```

---
