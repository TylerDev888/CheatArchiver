# Super Street Fighter IV

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM60203  
**Cheat Type:** Save Editor  

---

## Cheats

### Unlock All Normal Titles
**Author:**   
**Notes:** File: SAVEDATA

```
42004FA4 01010101
40740004 00000000
10005174 00000101
```

---

### Unlock All Ex Titles
**Author:**   
**Notes:** File: SAVEDATA

```
10005176 00000101
42005178 01010101
40070004 00000000
```

---

### Unlock All Character Colors
**Author:**   
**Notes:** File: SAVEDATA

```
42004D4C 01010101
40030004 00000000
```

---

### Update Crc32 (required)
**Author:**   
**Notes:** File: SAVEDATA  (set range:0x000004,0x01226B)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Swansave (required)
**Author:**   
**Notes:** File: SWANSAVE  (set range:0x000004,0x00C184)

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---

### Update Crc32 For Swanrply (required)
**Author:**   
**Notes:** File: SWANRPLY  (set range:0x000004,0x00AC25) (:SAVEDATA) ([Unlock All Normal Titles]) (42004FA4 01010101) (40740004 00000000) (10005174 00000101) ([Unlock All EX Titles]) (10005176 00000101) (42005178 01010101) (40070004 00000000) ([Unlock All Character Colors]) (42004D4C 01010101) (40030004 000...

```
set pointer:eof+1
set range:0x000004,pointer
set [hash]:CRC32
write at 0x000000:[hash]
```

---
