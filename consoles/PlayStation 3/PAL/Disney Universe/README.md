# Disney Universe

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01354  
**Cheat Type:** Save Editor  
**Source:** [From Game Genie For PS3](From Game Genie For PS3)  

---

## Cheats

### Max Money (not Working)
**Author:**   
**Notes:** File: BLES01354AUTOSAVE*\\56600001.DAT

```
80010008 60400000
00000002 00000000
28000008 05F5E0FF
```

---

### Get Crc32 For 56600001.dat (required)
**Author:**   
**Notes:** File: 56600001.DAT

```
set [hash_56600001.DAT]:CRC32
set [size_56600001.DAT]:eof+1
```

---

### Get Crc32 For 96600000.dat (required)
**Author:**   
**Notes:** File: 96600000.DAT  (dependency: SAVE.BIN)

```
set [hash_96600000.DAT]:CRC32
set [size_96600000.DAT]:eof+1
```

---

### Update Crc32 For 56600001.dat And 96600000.dat (required)
**Author:**   
**Notes:** File: SAVE.BIN

```
write at 0x000014:[size_56600001.DAT]
write at 0x000018:[hash_56600001.DAT]
write at 0x000024:[size_96600000.DAT]
write at 0x000028:[hash_96600000.DAT]
```

---
