# Minecraft

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01976  
**Cheat Type:** AP  

---

## Cheats

### Player Lvl 255
**Author:**   
**Notes:** File: GAMEDATA

```
search 0x58704C6576656C
write next (10):0xFF
search 0x58704C6576656C:1
write next (10):0xFF
search 0x58704C6576656C:2
write next (10):0xFF
search 0x58704C6576656C:3
write next (10):0xFF
```

---

### Turn Wooden Pickaxe To Diamond
**Author:**   
**Notes:** File: GAMEDATA

```
search 0x496E76656E746F7279
search next 0x010E
write next (0):0116
search 0x496E76656E746F7279:1
search next 0x010E
write next (0):0116
search 0x496E76656E746F7279:2
search next 0x010E
write next (0):0116
search 0x496E76656E746F7279:3
search next 0x010E
write next (0):0116
search 0x496E76656E746F7279:4
search next 0x010E
write next (0):0116
```

---

### Has Not Been In Creative
**Author:**   
**Notes:** File: GAMEDATA

```
search 0x6861734265656E496E4372656174697665
write next (17):0x00
```

---

### Get Crc32 Gamedata (required)
**Author:**   
**Notes:** File: GAMEDATA  (dependency: METADATA)

```
set [crc32_GAMEDATA]:crc32
```

---

### Update Crc32 On Metadata (required)
**Author:**   
**Notes:** File: METADATA  (Group: Update CRC32 Checksum (Required)) (:GAMEDATA) ([Get CRC32 GAMEDATA (Required)]) (set [crc32_GAMEDATA]:crc32) (dependency: METADATA) (:METADATA) ([Update CRC32 on METADATA (required)]) (write at 0xC:[crc32_GAMEDATA])

```
write at 0xC:[crc32_GAMEDATA]
```

---
