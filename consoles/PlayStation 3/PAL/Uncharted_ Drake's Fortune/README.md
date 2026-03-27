# Uncharted_ Drake's Fortune

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BCES00065  
**Cheat Type:** Save Editor  
**Source:** [GameGenie EU Codes](GameGenie EU Codes)  

---

## Cheats

### Unlock All Chapters
**Author:**   
**Notes:** File: BCES00064_NDI_UNCHARTED_DF_*\\USR-DATA

```
80010004 A5EF05C7
4A00001C 00000003
414F0020 00000000
```

---

### Update Crc32big:0 For Usr-data (required)
**Author:**   
**Notes:** File: BCES00064_NDI_UNCHARTED_DF_*\\USR-DATA

```
set range:0x000005,0x00DF41
set [hash]:CRC32Big:0
set [hash]:xor:FFFFFFFF
write at 0x000000:[hash]
```

---
