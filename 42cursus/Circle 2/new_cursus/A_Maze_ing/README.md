*This project has been created as part of the 42 curriculum by roandrie, rruiz*

## 📂 Description

**📜 Summary:**\
Create a **maze generator** that takes a configuration file, generates a maze and writes it to a file using a hexadecimal wall representation. The maze will also have a visual representation either in ASCII, or by using the minilibx. The maze will be generate randomly but can be reproduce via a **seed**.

**📝 Requierements**
- Each cell of the maze has between 0 and 4 walls, at each cardinal point (North,
Est, South, West).
- The entry and exist exist, are unique, are different, need to be inside the maze bounds.
- The maze is fully connected and do not have isolated cells. Walls must be at the external borders.
- The maze can't have large open areas: corridors can't be wider than 2 cells.
- The maze must contain a visible `42` wehen represented.
- If the `PERFECT` flag is activated, the maze must contain exactly one path between the entry and the exit
- The maze must be written in the output file using one hexadecimal digit per cell, where
each digit encodes which walls are closed:
- The maze generation must be implement as a **unique class**, a standalone module that can be imported in a future project.

|Bit|Direction|
|---|---|
|0|North|
|1|East|
|2|South|
|3|West|

Closed walls = 1 | Open = 0

**✏️ Visual representation**
- Use either the **terminal ASCII** or the **MiniLibX** library.
- The visual should clearly show walls, entry, exit and the solution path.

#### **User can**:
- Re-generate a new maze and display it.
- Show/Hide a valid shortest path from the entrance to the exit.
- Change maze wall colours.
- Set specific colours to display the `42` pattern.

**📮 Makefile:**\
This project must include a Makefile with strict following rules:
- `install`: Install all project dependencies using **pip**, **uv**, **pipx**, or any other package manager.
- `run`: Execute the main script of the project.
- `debug`: Run the main script in debug mode using Python`s built-in-debugger.
- `clean`: Remove all temporary files or caches.
- `lint`: Execute **flake8** (norme checker) and **mypy** (hint checker)
- `lint-strict`: Same as above but with **--strict**.

**🐍 Challenge:**
- Avoid any crashes and give clear error message.
- Prevent any leaks.
- Include type hint *(def func (name:str) -> bool)*. Use **Mypy** to check any potential error `pip install mypy`, then `mypy script.py`
- Include docstrings following **PEP 257** for better understanding.

## 🔷 Instructions

#### 1. First, clone this repository:
```bash
git clone https://github.com/Overtekk/push_swap
```
#### 2. Run the program:
```bash
python3 a_maze_ing.py config.txt
```

#### 📑 Configuration file format
You can configure your maze by using those keys:
|Key|Description|Example|
|:---|:---:|:---:|
|WIDTH| Maze width (number of cells)|WIDTH=20
|HEIGHT| Maze height| HEIGHT=15
|ENTRY| Entry coordinates (x,y)|ENTRY=0,0
|EXIT| Exit coordinates (x,y)|EXIT=19,14
|OUTPUT_FILE| Output filename|OUTPUT_FILE=maze.txt
|PERFECT| Is the maze perfect?|PERFECT=True

### 🤖 Maze generation algorithm:
#### Explanation:
wip
#### Why we choose this:
wip
#### Part of the code reusable, and how to do it:
wip


### 🧑‍🏫 The Team:
#### Roles of each team member:
wip
#### Anticipated planning, and the evolution:
wip
#### What worked well, what improvement could be done:
wip


### 📂 Specific tools:
wip


## 🐨 Status

Not completed yet

## 💿 Resources
-
