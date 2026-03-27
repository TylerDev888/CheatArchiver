# Yakuza Kiwami 3 & Dark Ties

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA54714  
**Cheat Type:** SaveWizard  

---

## Cheats

### Add Item Carry
**Author:**   
**Notes:** File: data\\.sav

```
search 0x22706C61796572223A
search next 0x2263617272795F6974656D22
search next 0x226D5F6C69737422
insert next A: \
```

---

### Add Item Box
**Author:**   
**Notes:** File: data\\.sav

```
search 0x22706C61796572223A
search next 0x22626F785F4974656D22
search next 0x226D5F6C69737422
insert next A: \
```

---

### Edit Points/Currencies
**Author:**   
**Notes:** File: data\\.sav

```
search 0x226D5F706F696E747322
search next 0x222E766572223A302C226D5F706F696E7422
search next 0x2C:([Points])
set pointer:pointer+1
delete next 0:until 0x2C
insert next 0: \
```

---
