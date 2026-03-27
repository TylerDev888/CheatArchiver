# BlazBlue_ Centralfiction

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES02230  
**Cheat Type:** Save Editor  

---

## Cheats

### Max P$ Money(by Bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
2000BBF8 0098967F
```

---

### Unlock All Gallery
**Author:**   
**Notes:** File: SYSTEM.DAT

```
420001C4 02020202
406E0004 00000000
```

---

### Unlock Test Voices
**Author:**   
**Notes:** File: SYSTEM.DAT

```
4000037C 00000002
40210001 00000000
```

---

### Update Wadd For System.dat (required)(by Bucanero)
**Author:**   
**Notes:** File: SYSTEM.DAT

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
