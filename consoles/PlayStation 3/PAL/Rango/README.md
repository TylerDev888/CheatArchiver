# Rango

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01164  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Progress.dat (required)
**Author:**   
**Notes:** File: PROGRESS.DAT  (set range:0xC,0x00001B)

```
set pointer:eof+1
set range:0xC,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Collect.dat (required)
**Author:**   
**Notes:** File: COLLECT.DAT  (set range:0xC,0x0007BB)

```
set pointer:eof+1
set range:0xC,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Options.dat (required)
**Author:**   
**Notes:** File: OPTIONS.DAT  (set range:0x00000C,0x00001B)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Chkpts.dat (required)
**Author:**   
**Notes:** File: CHKPTS.DAT  (set range:0x00000C,0x001393)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Achieve.dat (required)
**Author:**   
**Notes:** File: ACHIEVE.DAT  (set range:0x00000C,0x00019F)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---

### Update Crc32 For Upg.dat (required)
**Author:**   
**Notes:** File: UPG.DAT  (set range:0x00000C,0x00001C)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
