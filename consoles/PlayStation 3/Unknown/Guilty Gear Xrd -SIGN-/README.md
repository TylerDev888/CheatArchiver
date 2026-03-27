# Guilty Gear Xrd -SIGN-

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10289  
**Cheat Type:** Save Editor  

---

## Cheats

### Max Medals(by Easko)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
2000B5C4 0098967F
```

---

### Max W$ Money(by Bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
2000D6AC 0098967F
```

---

### Update Crc32 For System.dat (required)(by Chaoszage)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
set pointer:eof+1
set range:0x000010,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
