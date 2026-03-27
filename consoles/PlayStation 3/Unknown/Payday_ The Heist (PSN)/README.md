# Payday_ The Heist (PSN)

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** NPEA00331  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Md5 For Header.bin (required)
**Author:**   
**Notes:** File: HEADER.BIN  (set range:0x000004,0x000514)

```
set pointer:lastbyte-0xF
set range:0x000004,pointer
set [hash]:MD5
write next (0):[hash]
```

---

### Update Md5 For Info.bin (required)
**Author:**   
**Notes:** File: INFO.BIN  (set range:0x000004,0x00380B)

```
set pointer:lastbyte-0xF
set range:0x000004,pointer
set [hash]:MD5
write next (0):[hash]
```

---
