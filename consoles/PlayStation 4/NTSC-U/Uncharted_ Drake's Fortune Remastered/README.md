# Uncharted_ Drake's Fortune Remastered

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA02320  
**Cheat Type:** AP  
**Source:** [by bucanero](by bucanero)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  \\\\endian_swap(4) \\\\endian_swap(4) () (cheat codes go here) ()

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x00000C,[end]+0x0B
DECRYPT blowfish_ecb(\
```

---

### Update Crc32 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [block_length]:read(0x590,4)
set [block_length]:endian_swap
set [block_length]:[block_length]+0x58B
set range:0x590,[block_length]
set [hash]:crc32
set [hash]:endian_swap
write at 0x58C:[hash]
```

---

### Update Hmac Sha1 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set pointer:EOF-0x23
set range:0x00000C,pointer
set [hash]:hmac_sha1(\
write next (0):[hash]
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  \\\\endian_swap(4) \\\\endian_swap(4)

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x00000C,[end]+0x0B
ENCRYPT blowfish_ecb(\
```

---
