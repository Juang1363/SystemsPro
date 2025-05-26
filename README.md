# 🧠 SystemsPro: Juan's Systems Programming Gauntlet

Welcome to the **SystemsPro** repo – a chaotic good mix of C, Python, and a splash of assembly code forged through quests in systems programming. If you're into sockets, threading, signals, file I/O, and experimenting with system calls like you're gearing up for a boss fight, this is the dungeon for you. Think of this repo as my personal side quest log from a semester-long campaign in Systems Programming. No cheat codes, just trial, error, and a lot of `gcc`.

---
## 📜 Lore (aka Author)
Crafted by Juan Gonzalez, embedded systems programmer in training, HKN/IEEE Fratboy, and former Splatoon champ. This repo was part of my systems training arc—if you find a bug, it was probably the mini-boss I missed.

---

## 🎮 Table of Contents

- `client.c` / `server.c` – Classic TCP socket comms, like the Link Cable of the systems world.
- `TCPS.c` / `TCPC.py` – Cross-language multiplayer: talk C-to-Python like it's an in-game chat between platforms.
- `threading.c` / `threading_JG.py` – Multithreading examples, aka spawning helper threads like party members in a turn-based RPG.
- `signal.c` – Signal handling experiments. You’ll learn how to catch a `SIGINT` like it’s a thrown Pokéball.
- `copy_file.c` / `multiple_copies.c` – File I/O quests. Not as fun as collecting rupees, but still necessary for system mastery.
- `lab2.py`, `assignment3.*`, `assignment4.py` – Class assignment bosses.
- `battle_juan_gonzalez.py` – A Python battle simulator. 🧟‍♂️ vs 🐉, turn-based chaos, stats and all.
- `hash_juan_gonzalez.py` – Hashing mission. Almost as critical as your inventory screen.
- `triangle_juan_gonzalez.py.py` – Extra `.py` for good luck. Triangles, math, destiny.
- `popen.py` – Spawning subprocesses like it’s a summoning spell.
- `nop_slide.S` / `nop_slide.h` – Assembly time. Welcome to the **final boss zone**.
- `exam1.zip` / `exam2.c` – If you find exam files... shh, side quest spoilers.

---

## 🛠️ Requirements

No fancy gear needed. Just:
- GCC or Clang for the C files.
- Python 3.x
- A love of `man` pages and `strace`.

Build example:
```bash
gcc -o server server.c
gcc -o client client.c 
./server &
./client
```
## 🧩 Tips for Exploration
Feeling stuck? Try `strace` or `gdb`—they're like the "Scan" spell from RPGs. Know your enemy (bugs).

Mix and match the Python and C socket files for some cross-realm networking.

The `signal.c` file is surprisingly fun to tinker with—interrupt yourself and see how your program reacts.

---
## 🧠 Final Words

If you’ve read this far, you either really like systems programming... or just love a good reference. Either way, clone the repo and **git gud**.

🕹️ GGS,  
Juan
