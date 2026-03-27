# NBA 2K13

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** BLUS31028  
**Cheat Type:** AP  

---

## Cheats

### Max Fans
**Author:**   
**Notes:** File: USERDATA

```
2068833C 3B9AC9FF
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: USERDATA  (set range:0x000004,0x737206)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
