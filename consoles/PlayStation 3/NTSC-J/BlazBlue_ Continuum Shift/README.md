# BlazBlue_ Continuum Shift

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLJM60237  
**Cheat Type:** AP  
**Source:** [From Game Genie For PS3 & Keha World](From Game Genie For PS3 & Keha World)  

---

## Cheats

### Unlock All Gallery Visuals
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
42000160 02020202
40600004 00000000
```

---

### Unlock All Gallery Visuals (alt)
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
40000160 00000001
40D90001 00000000
```

---

### Challenge Mode Clear All Characters
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
400D45F0 00000001
41280001 00000000
```

---

### Story Mode Complete
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
42012622 FFFFFFFF
40500004 00000000
42000560 00000FFF
40100004 00000000
```

---

### Legion Mode Character 1 Unlimited And Health Max
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
000D48D3 00000002
200D48C8 00002710
200D48CC 00002710
```

---

### Legion Mode Character 2 Unlimited And Health Max
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
000D48E7 00000002
200D48DC 00002710
200D48E0 00002710
```

---

### Update Wadd Checksum (required)
**Author:**   
**Notes:** File: BLJM60237-SYSTEM\\SYSTEM.DAT

```
set [csum]:0
carry(2)
set pointer:eof+1
set [csum]:wadd(0x000004,pointer)
set [csum]:xor:FFFF
write at 0x000000:[csum]
```

---
