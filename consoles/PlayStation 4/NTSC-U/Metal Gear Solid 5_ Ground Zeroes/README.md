# Metal Gear Solid 5_ Ground Zeroes

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA00218  
**Cheat Type:** AP  
**Source:** [encryption/checksum by bucanero](encryption/checksum by bucanero)  

---

## Cheats

### CUSA00218 - Decrypt Save Data (required)
**Author:**   
**Notes:** [CUSA00218]  File: SAVE*

```
set range:0x0000,EOF+1
DECRYPT MGS5_TPP(0xEA11D524)
```

---

### CUSA00218 - Update Md5 Checksum (required)
**Author:**   
**Notes:** [CUSA00218]  File: SAVE*

```
set range:0x0010,EOF+1
set [hash]:MD5
write at 0x0000:[hash]
```

---

### CUSA00218 - Encrypt Save Data (required)
**Author:**   
**Notes:** [CUSA00218]  File: SAVE*

```
set range:0x0000,EOF+1
ENCRYPT MGS5_TPP(0xEA11D524)
```

---

### CUSA00211 - Decrypt Save Data (required)
**Author:**   
**Notes:** [CUSA00211]  File: SAVE*

```
set range:0x0000,EOF+1
DECRYPT MGS5_TPP(0xD2225CCB)
```

---

### CUSA00211 - Update Md5 Checksum (required)
**Author:**   
**Notes:** [CUSA00211]  File: SAVE*

```
set range:0x0010,EOF+1
set [hash]:MD5
write at 0x0000:[hash]
```

---

### CUSA00211 - Encrypt Save Data (required)
**Author:**   
**Notes:** [CUSA00211]  File: SAVE*

```
set range:0x0000,EOF+1
ENCRYPT MGS5_TPP(0xD2225CCB)
```

---
