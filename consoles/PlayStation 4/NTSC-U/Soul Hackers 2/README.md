# Soul Hackers 2

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA23630  
**Cheat Type:** SaveWizard  

---

## Cheats

### Edit A Demon's Skill 1
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
set pointer:pointer+11
delete next (0):until 0x2C
insert next (0):\
```

---

### Edit A Demon's Skill 2
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
search next 0x2C
set pointer:pointer+1
delete next (0):until 0x2C
insert next (0):\
```

---

### Edit A Demon's Skill 3
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
search next 0x2C:(2)
set pointer:pointer+1
delete next (0):until 0x2C
insert next (0):\
```

---

### Edit A Demon's Skill 4
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
search next 0x2C:(3)
set pointer:pointer+1
delete next (0):until 0x2C
insert next (0):\
```

---

### Edit A Demon's Skill 5
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
search next 0x2C:(4)
set pointer:pointer+1
delete next (0):until 0x2C
insert next (0):\
```

---

### Edit A Demon's Skill 6
**Author:**   
**Notes:** [Demon Skills]  File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x22536B696C6C4964223A5B:[Demon]
search next 0x2C:(5)
set pointer:pointer+1
delete next (0):until 0x5D
insert next (0):\
```

---

### Change A Demon's Race
**Author:**   
**Notes:** File: data\\.dat

```
search 0x224E616B616D6153746F636B22
search next 0x7B224964223A:[Demon]
set pointer:pointer+6
delete next (0):until 0x2C
insert next (0):\
```

---
