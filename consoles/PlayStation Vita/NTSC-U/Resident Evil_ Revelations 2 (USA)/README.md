# Resident Evil_ Revelations 2 (USA)

**Console:** PlayStation Vita  
**Region:** NTSC-U  
**Serial:** PCSE00608  
**Cheat Type:** Save Editor  
**Source:** [Credits: Bucanero](Credits: Bucanero)  

---

## Cheats

### Decompress Data0000.bin (required)
**Author:**   
**Notes:** File: data/data0000.bin  \\\\Decompress(0x00000000, 15)

---

### Update Dwadd Checksum (required)
**Author:**   
**Notes:** File: ~extracted\\00000000.dat

```
set [csum]:0
set [csum]:dwadd_le(0x000010,0x1279AF)
set [csum]:endian_swap
write at 0x000008:[csum]
```

---

### Update Sha1 Hash (required)
**Author:**   
**Notes:** File: ~extracted\\00000000.dat  (set range:0x000010,0x1279AF) (set [hash]:SHA1) (write at 0x127590:[hash]) \\\\endian_swap(4)

```
set pointer:eof-0x1F
set range:0x0010,pointer
set [hash]:SHA1
write next (0):[hash]
set range:pointer,pointer+0x14
```

---

### Fix Compression (required)
**Author:**   
**Notes:** File: data/data0000.bin  \\\\delete at 0x00:0x4000

---

### Compress Data0000.bin (required)
**Author:**   
**Notes:** File: data/data0000.bin  \\\\Compress(0x00000000)

---
