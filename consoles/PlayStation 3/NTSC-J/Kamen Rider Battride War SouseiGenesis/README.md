# Kamen Rider Battride War SouseiGenesis

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** NPJB00758  
**Cheat Type:** Save Editor  

---

## Cheats

### Shop Points 9999999
**Author:**   
**Notes:** File: SAVEDATA.DAT

```
20000124 0098967F
```

---

### Rider Souls 9999999
**Author:**   
**Notes:** File: SAVEDATA.DAT

```
20000128 0098967F
```

---

### Update Crc32big For Savedata.dat (required)
**Author:**   
**Notes:** File: SAVEDATA.DAT  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes) (set range:0x000004,0x22EC67)

```
write at 0x000004:00000000
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32Big
write at 0x000004:[hash]
```

---
