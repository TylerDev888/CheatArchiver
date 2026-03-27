# SpongeBob SquarePants_ Plankton's Robotic Revenge

**Console:** PlayStation 3  
**Region:** PAL  
**Serial:** BLES01911  
**Cheat Type:** Save Editor  
**Source:** [From SHAkA](From SHAkA)  

---

## Cheats

### 99,999,999 Botls - Spongegbob
**Author:**   
**Notes:** File: SBSP_0

```
search 0x5846E8C7
write next 0x4:05F5E0FF
```

---

### 99,999,999 Botls - Mr Krabs
**Author:**   
**Notes:** File: SBSP_0

```
search 0x51AD48BD
write next 0x4:05F5E0FF
```

---

### 99,999,999 Botls - Patric
**Author:**   
**Notes:** File: SBSP_0

```
search 0xB78483F9
write next 0x4:05F5E0FF
```

---

### 99,999,999 Botls - Sandy
**Author:**   
**Notes:** File: SBSP_0

```
search 0x5CB338FA
write next 0x4:05F5E0FF
```

---

### 99,999,999 Botls - Squidward
**Author:**   
**Notes:** File: SBSP_0

```
search 0xB37153C4
write next 0x4:05F5E0FF
```

---

### Update Crc32 For Sbsp_0 (required)
**Author:**   
**Notes:** File: SBSP_0  (set range:0x00000C,0x00014F)

```
set pointer:eof+1
set range:0x00000C,pointer
set [hash]:CRC32
write at 0x000004:[hash]
```

---
