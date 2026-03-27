# GoldenEye 007_ Reloaded

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01292  
**Cheat Type:** Save Editor  
**Source:** [GameGenie EU Codes](GameGenie EU Codes)  

---

## Cheats

### Infinite Ammo
**Author:**   
**Notes:** File: BLES01292AUTOSAVE*\\66600001.DAT

```
80010004 5CABFACE
93000000 00000014
18000000 00007FFF
18000006 00007FFF
1800000C 00007FFF
```

---

### Get Crc32 & File Size Of 66600001.dat (required)
**Author:**   
**Notes:** File: BLES01292AUTOSAVE*\\66600001.DAT

```
set [crc32_66600001.DAT]:crc32
set [size_66600001.DAT]:eof+1
```

---

### Get Crc32 & File Size Of 96600000.dat (required)
**Author:**   
**Notes:** File: BLES01292AUTOSAVE*\\96600000.DAT  (dependency: SAVE.BIN)

```
set [crc32_96600000.DAT]:crc32
set [size_96600000.DAT]:eof+1
```

---

### Update Crc32 On Save.bin (required)
**Author:**   
**Notes:** File: BLES01292AUTOSAVE*\\SAVE.BIN  ([Update CRC32 for SAVE.BIN]) (set range:0x10,0x000223)

```
write at 0x14:[size_66600001.DAT]
write at 0x18:[crc32_66600001.DAT]
write at 0x24:[size_96600000.DAT]
write at 0x28:[crc32_96600000.DAT]
set pointer:eof+1
set range:0x10,pointer
set [hash]:CRC32
write at 0x000008:[hash]
```

---
