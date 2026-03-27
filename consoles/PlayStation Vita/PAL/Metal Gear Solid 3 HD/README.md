# Metal Gear Solid 3 HD

**Console:** PlayStation Vita  
**Region:** PAL  
**Serial:** PCSB00176  
**Cheat Type:** Save Editor  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decode Master.bin (required)
**Author:**   
**Notes:** [Decrypt Mgs3]  File: *MASTER.BIN

```
set range:0x0000,0x001F
DECRYPT mgs_base64
```

---

### Decrypt Data.bin (required)
**Author:**   
**Notes:** [Decrypt Mgs3]  File: *DATA.BIN

```
set range:0x000000,0x00497B
DECRYPT mgs(\
```

---

### Encrypt Data.bin (required)
**Author:**   
**Notes:** [Encrypt Mgs3]  File: *DATA.BIN

```
set range:0x000000,0x00497B
set [master_hash]:CRC32
ENCRYPT mgs(\
```

---

### Encode Master.bin (required)
**Author:**   
**Notes:** [Encrypt Mgs3]  File: *MASTER.BIN

```
write at 0x0008:[master_hash]
write at 0x0010:[master_hash]
set range:0x0000,0x001F
ENCRYPT mgs_base64
```

---
