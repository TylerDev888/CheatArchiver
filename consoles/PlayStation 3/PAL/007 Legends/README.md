# 007 Legends

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01614  
**Cheat Type:** Save Editor  

---

## Cheats

### Get Crc32 For 66600000.dat
**Author:**   
**Notes:** File: 66600000.DAT

```
set [hash_66600000.DAT]:CRC32
set [size_66600000.DAT]:eof+1
```

---

### Get Crc32 For 66600001.dat
**Author:**   
**Notes:** File: 66600001.DAT

```
set [hash_66600001.DAT]:CRC32
set [size_66600001.DAT]:eof+1
```

---

### Get Crc32 For 66600008.dat
**Author:**   
**Notes:** File: 66600008.DAT

```
set [hash_66600008.DAT]:CRC32
set [size_66600008.DAT]:eof+1
```

---

### Get Crc32 For 96600000.dat
**Author:**   
**Notes:** File: 96600000.DAT

```
set [hash_96600000.DAT]:CRC32
set [size_96600000.DAT]:eof+1
```

---

### Update Crc32 For Dat Files
**Author:**   
**Notes:** File: SAVE.BIN

```
write at 0x000014:[size_66600000.DAT]
write at 0x000018:[hash_66600000.DAT]
write at 0x000024:[size_66600001.DAT]
write at 0x000028:[hash_66600001.DAT]
write at 0x000034:[size_66600008.DAT]
write at 0x000038:[hash_66600008.DAT]
write at 0x000044:[size_96600000.DAT]
write at 0x000048:[hash_96600000.DAT]
```

---
