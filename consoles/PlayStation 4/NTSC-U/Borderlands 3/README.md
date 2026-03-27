# Borderlands 3

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA07823  
**Cheat Type:** AP  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decrypt Profile (required)
**Author:**   
**Notes:** File: profile  (use profile xor keys)

```
search \
set [size]:read(pointer+0x17,4)
set [size]:endian_swap
set [size]:[size]+0x1A
set range:pointer+0x1B,pointer+[size]
DECRYPT borderlands3(0)
```

---

### Decrypt Save-game
**Author:**   
**Notes:** File: *  (use save-game xor keys) () (cheat codes go here) ()

```
search \
set [size]:read(pointer+0x0C,4)
set [size]:endian_swap
set [size]:[size]+0x0F
set range:pointer+0x10,pointer+[size]
DECRYPT borderlands3(1)
```

---

### Encrypt Profile (required)
**Author:**   
**Notes:** File: profile

```
search \
set [size]:read(pointer+0x17,4)
set [size]:endian_swap
set [size]:[size]+0x1A
set range:pointer+0x1B,pointer+[size]
ENCRYPT borderlands3(0)
```

---

### Encrypt Save-game
**Author:**   
**Notes:** File: *

```
search \
set [size]:read(pointer+0x0C,4)
set [size]:endian_swap
set [size]:[size]+0x0F
set range:pointer+0x10,pointer+[size]
ENCRYPT borderlands3(1)
```

---
