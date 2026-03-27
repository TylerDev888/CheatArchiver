# Sacred 3

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01492  
**Cheat Type:** Save Editor  
**Source:** [by pupped](by pupped)  

---

## Cheats

### Level 50
**Author:**   
**Notes:** [1st Character]  File: SVDAT00.BIN

```
write at 0x00000124:0x3B9AC9FF
```

---

### Max Money
**Author:**   
**Notes:** [1st Character]  File: SVDAT00.BIN

```
write at 0x00000128:0x3B9AC9FF
```

---

### 99 Items 1st Character
**Author:**   
**Notes:** [1st Character]  File: SVDAT00.BIN

```
write at 0x00001550:0x63636363
write at 0x00001554:0x63636363
write at 0x00001558:0x63636363
```

---

### 99 Items 2nd Character
**Author:**   
**Notes:** [2nd Character]  File: SVDAT00.BIN

```
write at 0x00002AC0:0x63636363
write at 0x00002AC4:0x63636363
write at 0x00002AC8:0x63636363
```

---

### 99 Items
**Author:**   
**Notes:** [3rd Character]  File: SVDAT00.BIN

```
write at 0x00004030:0x63636363
write at 0x00004034:0x63636363
write at 0x00004038:0x63636363
```

---

### Update Crc32 For Svdat00.bin (required)
**Author:**   
**Notes:** [Checksum Fixer]  File: SVDAT00.BIN  (Checksum offset is located within the checksum range.) (Initializing checksum with null bytes)

```
write at 0x000004:00000000
;set range:0x000000,0x0111C7
set pointer:eof+1
set range:0x000000,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
