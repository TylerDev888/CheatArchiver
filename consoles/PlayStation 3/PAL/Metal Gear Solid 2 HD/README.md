# Metal Gear Solid 2 HD

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01419  
**Cheat Type:** Save Editor  
**Source:** [Metal Gear Solid 3 HD](Metal Gear Solid 3 HD)  

---

## Cheats

### Decode Master.bin (required)
**Author:**   
**Notes:** [Decrypt]  File: MASTER.BIN

```
set range:0x0000,eof+1
DECRYPT mgs_base64
```

---

### Decrypt Data.bin (required)
**Author:**   
**Notes:** [Decrypt]  File: DATA.BIN  (decrypt 2nd layer) (cheats should go here)

```
set range:0x000004,0x0071A9
DECRYPT mgs(\
set range:0x000004,0x00159B
DECRYPT mgs(0x00)
set range:0x0015AA,0x0031A9
DECRYPT mgs(0x00)
set range:0x0031AA,0x0071A9
DECRYPT mgs(0x00)
```

---

### Update Custom Checksum (required)
**Author:**   
**Notes:** [Encrypt]  File: DATA.BIN

```
set range:0x000004,0x00159B
set [crc1]:mgs2_checksum
set range:0x0015AA,0x0031A9
set [crc2]:mgs2_checksum
set [crc1]:xor:[crc2]
write at 0x0015A6:[crc1]
```

---

### Encrypt Data.bin (required)
**Author:**   
**Notes:** [Encrypt]  File: DATA.BIN  (encrypt 2nd layer)

```
set range:0x000004,0x00159B
ENCRYPT mgs(0x00)
set range:0x0015AA,0x0031A9
ENCRYPT mgs(0x00)
set range:0x0031AA,0x0071A9
ENCRYPT mgs(0x00)
set range:0x000004,0x0071A9
set [master_hash]:CRC32
ENCRYPT mgs(\
```

---

### Encode Master.bin (required)
**Author:**   
**Notes:** [Encrypt]  File: MASTER.BIN

```
write at 0x0010:[master_hash]
set range:0x0000,eof+1
ENCRYPT mgs_base64
```

---
