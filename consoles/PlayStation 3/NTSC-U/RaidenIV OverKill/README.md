# RaidenIV OverKill

**Console:** PlayStation 3  
**Region:** NTSC-U  
**Serial:** NPUB31371  
**Cheat Type:** Save Editor  

---

## Cheats

### 99 Bombs+99 Lives(by Vesper)
**Author:**   
**Notes:** File: TEST0

```
write at 0x0002A117:63
write at 0x0002A11B:63
```

---

### 42 Lives(by Vesper)
**Author:**   
**Notes:** File: TEST0

```
write at 0x0002A117:2A
```

---

### Update Add For Test0 (required)
**Author:**   
**Notes:** File: TEST0  (set [csum]:add(0x000004,0x02A407)) (Warnings:) (entering the option screen hangs the game) (picking up 1ups immediately put you to 7 lives (do not save all the fairies in M1 or destroy 1000+ meteors in M2, unless you need to do that for the trophies, or you'll receive also a 1up as ...

```
set [csum]:0
set pointer:eof+1
set [csum]:add(0x000004,pointer)
write at 0x000000:[csum]
```

---
