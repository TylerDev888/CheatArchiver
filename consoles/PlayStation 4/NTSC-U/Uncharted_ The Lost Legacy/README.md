# Uncharted_ The Lost Legacy

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA07875  
**Cheat Type:** AP  
**Source:** [decryption/checksums: by bucanero](decryption/checksums: by bucanero)  

---

## Cheats

### Decrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA  () (add cheat codes here) ()

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x000008,[end]+7
DECRYPT blowfish_ecb(\
```

---

### Update Crc32 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [block_length]:read(0x58C,4)
set [block_length]:endian_swap
set [block_length]:[block_length]+0x587
set range:0x58C,[block_length]
set [hash]:crc32
set [hash]:endian_swap
write at 0x588:[hash]
```

---

### Update Hmac Sha1 Checksum For Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set pointer:EOF-0x1F
set range:0x000008,pointer
set [hash]:hmac_sha1(\
write next (0):[hash]
```

---

### Encrypt Usr-data (required)
**Author:**   
**Notes:** File: USR-DATA

```
set [end]:read(EOF-3, 4)
set [end]:endian_swap
set range:0x000008,[end]+7
ENCRYPT blowfish_ecb(\
```

---
