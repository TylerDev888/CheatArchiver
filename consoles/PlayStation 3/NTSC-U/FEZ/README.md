# FEZ

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31448  
**Cheat Type:** Save Editor  

---

## Cheats

### Default:update Settings For Save.dat
**Author:**   
**Notes:** File: SAVE.DAT

```
search \
set [begin]:pointer+0x20
set [size]:read([begin],4)
set [end_of_range]:[begin]+[size]-1
set [begin]:[begin]+4
set range:[begin],[end_of_range]
set [hash]:CRC32
set pointer:[end_of_range]+1
write next (0):[hash]
```

---

### Default:update Saveslot0 For Save.dat
**Author:**   
**Notes:** File: SAVE.DAT

```
search \
set [begin]:pointer+0x20
set [size]:read([begin],4)
set [end_of_range]:[begin]+[size]-1
set [begin]:[begin]+4
set range:[begin],[end_of_range]
set [hash]:CRC32
set pointer:[end_of_range]+1
write next (0):[hash]
```

---

### Default:update Saveslot1 For Save.dat
**Author:**   
**Notes:** File: SAVE.DAT

```
search \
set [begin]:pointer+0x20
set [size]:read([begin],4)
set [end_of_range]:[begin]+[size]-1
set [begin]:[begin]+4
set range:[begin],[end_of_range]
set [hash]:CRC32
set pointer:[end_of_range]+1
write next (0):[hash]
```

---

### Default:update Saveslot2 For Save.dat
**Author:**   
**Notes:** File: SAVE.DAT

```
search \
set [begin]:pointer+0x20
set [size]:read([begin],4)
set [end_of_range]:[begin]+[size]-1
set [begin]:[begin]+4
set range:[begin],[end_of_range]
set [hash]:CRC32
set pointer:[end_of_range]+1
write next (0):[hash]
```

---

### Default:update Saveslot3 For Save.dat
**Author:**   
**Notes:** File: SAVE.DAT

```
search \
set [begin]:pointer+0x20
set [size]:read([begin],4)
set [end_of_range]:[begin]+[size]-1
set [begin]:[begin]+4
set range:[begin],[end_of_range]
set [hash]:CRC32
set pointer:[end_of_range]+1
write next (0):[hash]
```

---
