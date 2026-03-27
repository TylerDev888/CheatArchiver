# Sports Champions

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES01012  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Crc32 For Stats.bin (required)
**Author:**   
**Notes:** File: STATS.BIN  (set range:0x000004,0x000BFE)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Resume.bin (required)
**Author:**   
**Notes:** File: RESUME.BIN  (set range:0x000004,0x00330F)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For User0.bin (required)
**Author:**   
**Notes:** File: USER0.BIN  (set range:0x000004,0x00FC97)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Vp_gd_bc.bin (required)
**Author:**   
**Notes:** File: VP_GD_BC.BIN  (set range:0x000004,0x09607F)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
