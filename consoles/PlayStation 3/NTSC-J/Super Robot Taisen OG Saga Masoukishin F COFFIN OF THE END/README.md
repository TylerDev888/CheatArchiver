# Super Robot Taisen OG Saga Masoukishin F COFFIN OF THE END

**Console:** PlayStation 3  
**Region:** NTSC-J  
**Serial:** BLAS50731  
**Cheat Type:** Save Editor  

---

## Cheats

### Red:use 1 Cheat At A Time Only
**Author:**   
**Notes:** File: DATA-BIN

---

### Red:always Go To Option Setting And Set The Setting Before Going To Battle,let Increase To 3 Byte Again Else It Will Be Frozen
**Author:**   
**Notes:** File: DATA-BIN

---

### More Gold, Setting<->gold
**Author:**   
**Notes:** [Quick Mode]  File: DATA-BIN

```
set [G]:read(0x48F0,4)
set [S]:read(0x48E8,4)
write at 0x48F0:[S]
write at 0x48E8:[G]
```

---

### Red:please Visit Http://bruteforcesavedata.forumms.net/t1139-super-robot-taisen-og-saga-masoukishin-f-coffin-of
**Author:**   
**Notes:** [Manual Mode]  File: DATA-BIN

---

### 4byte Swap,fill In Your Desire Cheat Into 0xaaaa
**Author:**   
**Notes:** [Manual Mode]  File: DATA-BIN

```
set [G]:read(0xAAAA,4)
set [S]:read(0x48E8,4)
write at 0xAAAA:[S]
write at 0x48E8:[G]
```

---

### 2byte Swap,fill In Your Desire Cheat Into 0xaaaa(partial Working)
**Author:**   
**Notes:** [Manual Mode]  File: DATA-BIN

```
set [G]:read(0xAAAA,2)
set [S]:read(0x495E,2)
write at 0xAAAA:[S]
write at 0x495E:[G]
```

---
