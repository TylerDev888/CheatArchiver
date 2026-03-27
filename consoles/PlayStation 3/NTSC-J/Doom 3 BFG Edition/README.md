# Doom 3 BFG Edition

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLAS50531  
**Cheat Type:** Save Editor  

---

## Cheats

### Update Md5_xor For _checkpt (required)
**Author:**   
**Notes:** File: _CHECKPT  (set range:0x000000,0x0738E6) (write at 0x0738E7:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---

### Update Md5_xor For _strings (required)
**Author:**   
**Notes:** File: _STRINGS  (set range:0x000000,0x028005) (write at 0x028006:[hash])

```
set pointer:eof-3
set range:0x000000,pointer
set [hash]:MD5_XOR
set pointer:eof-3
write next (0):[hash]
```

---
