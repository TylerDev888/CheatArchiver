# Dark Void

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00723  
**Cheat Type:** AP  
**Source:** [From zeick](From zeick)  

---

## Cheats

### Decompress Profile.dvp (required)
**Author:**   
**Notes:** File: PROFILE.DVP

```
Decompress(0x00000020, 15)
```

---

### 999999 Points
**Author:**   
**Notes:** File: ~extracted\\00000020.dat

```
write at 0x0000004C:0x000F423F
```

---

### Fix Compression
**Author:**   
**Notes:** File: BLES00723_PROFILE\\PROFILE.DVP

```
delete at 0x30:0x4FF
```

---

### Compress Profile.dvp (required)
**Author:**   
**Notes:** File: BLES00723_PROFILE\\PROFILE.DVP

```
Compress(0x00000020)
```

---

### Update Sha1 For Profile.dvp (required)
**Author:**   
**Notes:** File: BLES00723_PROFILE\\PROFILE.DVP

```
set pointer:eof+1
set range:0x00001C,pointer
set [hash]:SHA1
write at 0x000008:[hash]
```

---

### Update Crc32big For Profile.dvp (required)
**Author:**   
**Notes:** File: BLES00723_PROFILE\\PROFILE.DVP

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---

### Update Crc32big For Chkpt.sav (required)
**Author:**   
**Notes:** File: BLES00723_SAVE_AUTOSAVE\\CHKPT.SAV  (set range:0x000008,0x009743)

```
set pointer:eof+1
set range:0x000008,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---
