# Metal Gear Solid 5_ Ground Zeroes

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01971  
**Cheat Type:** AP  
**Source:** [encryption/checksum by bucanero](encryption/checksum by bucanero)  

---

## Cheats

### Decrypt Save Data (required)
**Author:**   
**Notes:** File: SAVE*  (codes go here)

```
set range:0x0000,EOF+1
DECRYPT MGS5_TPP(0xE13943C4)
```

---

### Update Md5 Checksum (required)
**Author:**   
**Notes:** File: SAVE*

```
set range:0x0010,EOF+1
set [hash]:MD5
write at 0x0000:[hash]
```

---

### Encrypt Save Data (required)
**Author:**   
**Notes:** File: SAVE*

```
set range:0x0000,EOF+1
ENCRYPT MGS5_TPP(0xE13943C4)
```

---
