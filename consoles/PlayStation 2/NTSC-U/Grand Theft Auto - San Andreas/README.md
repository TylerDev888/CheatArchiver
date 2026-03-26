# Grand Theft Auto - San Andreas

**Console:** PlayStation 2  
**Region:** NTSC-U  
**Serial:** SLUS-20946  
**Source:** [gamehacking.org](https://gamehacking.org/game/44)  

---

## Cheats

### Master Code
**Author:** ReallyCoolName  
**Notes:** Must be active for all other codes to work.

```
F0100008 0000000E
```

---

### Infinite Health
**Author:** GodModeGuy

```
2A456B10 000000C8
```

---

### Infinite Ammo
**Author:** GodModeGuy

```
2058B650 05F5E0FF
2058B654 05F5E0FF
```

---

### Infinite Health (Pointer-based)
**Author:** PointerPro  
**Notes:** Follows a pointer chain from the player base to the health field.

**Pointer chain:**
```
Base [Player Pointer]:   203F8A00 00000000
  -> +0x14  [Player Ped Object]
  -> +0x900  [Health]
Final [Max Health Value]:   2058B610 461C4000
```

---

### All Weapons (Pointer-based)
**Author:** PointerPro  
**Notes:** Follows a pointer chain to the player weapon slot.

**Pointer chain:**
```
Base [Player Pointer]:   203F8A00 00000000
  -> +0x14  [Player Ped Object]
  -> +0x3C  [Weapon Slot Base]
Final [Weapon ID]:   1058B600 00000009
```

---

### Wanted Level - Never Wanted
**Author:** LawlessCoder

```
204A5680 00000000
```

---

## Patches

| Patch |
|---|
| [NTSC-U-Patch-v1.0](./patches/NTSC-U-Patch-v1.0/) |
