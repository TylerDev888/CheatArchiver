# Patapon 3

**Console:** PSP  
**Region:** PAL  
**Serial:** UCES01421  
**Cheat Type:** Save Editor  
**Source:** [encryption by bucanero](encryption by bucanero)  

---

## Cheats

### Decrypt Secure.bin (required)
**Author:**   
**Notes:** File: SECURE.BIN  (// mods should go here)

```
set range:0x0000,EOF+1
DECRYPT camellia_ecb(\
```

---

### Encrypt Secure.bin (required)
**Author:**   
**Notes:** File: SECURE.BIN  (CWCheats) () (_C1 # Disable Save Hash Check) (_L 0xD0235CB0 0x00000018) (_L 0x20235CB0 0x8E050000) (_L 0xD0235FA4 0x00000018) (_L 0x20235FA4 0x8E050000) () (# Original code by Owocek) (# Adapted to USA by Madwig) (# The code works on EUR / USA) (# After saving once code is not ...

```
set range:0x0000,EOF+1
ENCRYPT camellia_ecb(\
```

---
