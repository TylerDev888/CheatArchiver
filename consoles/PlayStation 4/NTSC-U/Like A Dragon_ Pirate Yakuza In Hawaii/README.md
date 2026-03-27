# Like A Dragon_ Pirate Yakuza In Hawaii

**Console:** PlayStation 4  
**Region:** NTSC-U  
**Serial:** CUSA49939  
**Cheat Type:** SaveWizard  

---

## Cheats

### Add Item (jsmin Sw)
**Author:**   
**Notes:** File: save[0-9]+\\data.sav

```
search 0x22706C61796572223A
search next 0x2263617272795F6974656D22
search next 0x226D5F6C69737422
Insert Next A: \
```

---

### Add Item (json)
**Author:**   
**Notes:** File: save[0-9]+\\data.sav

```
search 0x22706C61796572223A207B
search next 0x2263617272795F6974656D22
search next 0x226D5F6C69737422
Insert Next 1C: \
```

---

### Edit Points/Currencies
**Author:**   
**Notes:** File: save[0-9]+\\data.sav

```
search 0x226D5F706F696E747322
search next 0x222E766572223A302C226D5F706F696E7422
search next 0x2C:([Points])
set pointer:pointer+1
delete next 0:until 0x2C
insert next 0: \
```

---
