# Yu-Gi-Oh! 5D's Decade Duels Plus (PSN)

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB30903  
**Cheat Type:** Save Editor  
**Source:** [Code created by Zephyer - Checksum created by Zeick](Code created by Zephyer - Checksum created by Zeick)  

---

## Cheats

### Have All Cards (x3)
**Author:**   
**Notes:** File: AUTOSAVE

```
400020F0 00000006
4F3C0004 00000000
```

---

### Default:update Crc32 (required)
**Author:**   
**Notes:** File: AUTOSAVE

```
set range:0x10,0x5E50
set [hash]:crc32
write at 0x0C:[hash]
write at 0x0C:xor:B7554EF7
```

---
