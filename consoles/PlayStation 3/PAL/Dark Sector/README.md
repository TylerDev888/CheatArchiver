# Dark Sector

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES00222  
**Cheat Type:** AP  

---

## Cheats

### Update Md5 For 01.sav (required)
**Author:**   
**Notes:** File: BLES00222\\??.SAV  (set range:0x000010,0x0158CB)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:MD5
write at 0x000000:[hash]
```

---

### Update Md5 For Settings (required)
**Author:**   
**Notes:** File: SETTINGS  (set range:0x000010,0x0005F5)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:MD5
write at 0x000000:[hash]
```

---

### Update Md5 For Continue.sav (required)
**Author:**   
**Notes:** File: CONTINUE.SAV  (set range:0x000010,0x010568)

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:MD5
write at 0x000000:[hash]
```

---
