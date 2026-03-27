# Grand Theft Auto V

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA00411  
**Cheat Type:** AP  
**Source:** [by bucanero, ChendoChap](by bucanero, ChendoChap)  

---

## Cheats

### Aes Decrypt Memory.dat (required)
**Author:**   
**Notes:** File: memory.dat  () (cheat values are big-endian) ()

```
set [end]:read(0x108,4)
set range:0x000114,[end]+0x0113
DECRYPT aes_ecb(0x1685FFA38D010F0DFE661CF9B5572C500D802648DB37B9ED0F48C57342C022F5)
```

---

### Franklin Money 999999999
**Author:**   
**Notes:** File: memory.dat

```
80010004 44BD6982
28000004 FFC99A3B
```

---

### Michael Money 999999999
**Author:**   
**Notes:** File: memory.dat

```
80010004 0324C31D
28000004 FFC99A3B
```

---

### Trevor Money 999999999
**Author:**   
**Notes:** File: memory.dat

```
80010004 8D75047D
28000004 FFC99A3B
```

---

### Update Chks Checksum (required)
**Author:**   
**Notes:** File: memory.dat

```
set range:0x000000,eof+1
set [chks]:rockstar_checksum
```

---

### Aes Encrypt Memory.dat (required)
**Author:**   
**Notes:** File: memory.dat

```
set [end]:read(0x108,4)
set range:0x000114,[end]+0x0113
ENCRYPT aes_ecb(0x1685FFA38D010F0DFE661CF9B5572C500D802648DB37B9ED0F48C57342C022F5)
```

---
