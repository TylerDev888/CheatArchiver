# Macross 30_ Ginga o Tsunagu Utagoe

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10184  
**Cheat Type:** Save Editor  
**Source:** [From KE-HA, Sixthman & Pu](From KE-HA, Sixthman & Pu)  

---

## Cheats

### Kitai Kaihatsu All Unlock(from Ke-ha)
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
40047A00 000000FF
40800001 00000000
```

---

### Money 999,999,999
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
20047B48 5F5E0FF
```

---

### Exp 9999999 - Leon Sakaki
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
20092BB0 0098967F
```

---

### Exp 9999999 - Aisha Blanchette
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
20092C10 0098967F
```

---

### Exp 9999999 - Mina Forte
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
20092C70 0098967F
```

---

### Money 2byte Exchange(from Sixthman)
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
51047B4A 00000002
51047B48 00000000
10047B4A 00000000
```

---

### Exp 2byte Exchange - Leon Sakaki
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
51092BB2 00000002
51092BB0 00000000
10092BB2 00000000
```

---

### Exp 2byte Exchange - Aisha Blanchette(from Pu)
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
51092C12 00000002
51092C10 00000000
10092C12 00000000
```

---

### Exp 2byte Exchange - Mina Forte
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
51092C72 00000002
51092C70 00000000
10092C72 00000000
```

---

### Update Add Checksum For Savedata.bin (required)
**Author:**   
**Notes:** File: SAVEDATA.BIN

```
set [csum]:0
set [csum]:add(0x000000,0x0479EB)
set [csum]:right([csum],2)
write at 0x0479EC:[csum]
set [csum]:0
set [csum]:add(0x0479F0,0x093CDB)
set [csum]:right([csum],2)
write at 0x093CDC:[csum]
```

---
