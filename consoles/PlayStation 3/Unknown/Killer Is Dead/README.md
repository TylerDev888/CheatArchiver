# Killer Is Dead

**Console:** PlayStation 3  
**Region:** Unknown  
**Serial:** BLJS10215  
**Cheat Type:** AP  
**Source:** [From Bokosuka Games](From Bokosuka Games)  

---

## Cheats

### Moon Crystal 9999
**Author:**   
**Notes:** File: PAYLOAD

```
search 0x4D696E6572616C5F41:1
write next C: 270F
search 0x4D696E6572616C5F41:2
write next C: 270F
search 0x4D696E6572616C5F41:3
write next C: 270F
search 0x4D696E6572616C5F41:4
write next C: 270F
```

---

### Health Lv.99
**Author:**   
**Notes:** File: PAYLOAD

```
search 0x4D696E6572616C5F42:1
write next C: 270F
search 0x4D696E6572616C5F42:2
write next C: 270F
search 0x4D696E6572616C5F42:3
write next C: 270F
search 0x4D696E6572616C5F42:4
write next C: 270F
```

---

### Blood Lv.99
**Author:**   
**Notes:** File: PAYLOAD

```
search 0x4D696E6572616C5F43:1
write next C: 270F
search 0x4D696E6572616C5F43:2
write next C: 270F
search 0x4D696E6572616C5F43:3
write next C: 270F
search 0x4D696E6572616C5F43:4
write next C: 270F
```

---

### Cash 99,999,999
**Author:**   
**Notes:** File: PAYLOAD

```
search 0x01332B:2
write next 8: 05F5E0FF
```

---

### Default:update Crc32 (required)
**Author:**   
**Notes:** File: PAYLOAD

```
set pointer:eof-3
set range:0x0, pointer
set [crc]:crc32big
set pointer:eof-3
write next (0):[crc]
```

---
