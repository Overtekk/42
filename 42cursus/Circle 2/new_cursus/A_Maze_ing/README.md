*This project has been created as part of the 42 curriculum by roandrie, rruiz*

## Quick Start
```bash
# Create virtual environnement and install dependencies
make all

# or just install dependencies
make install

# Run the script with the default configuration
make run

# Clean build artifacts
make clean
```

---

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
git clone https://github.com/Overtekk/A_Maze_ing
```
#### 2. Run the program:
##### by using the Makefile
```bash
make all
source .venv/bin/activate
make run
```
##### or (make sur to create a virtual environnement and check if dependencies are installed)
```bash
python3 a_maze_ing.py config.txt
```

---

## 📑 Configuration file format
You can configure your maze by using those keys:

|Key|Description|Example|
|:---|:---:|:---:|
|WIDTH| Maze width (number of cells)|WIDTH=20
|HEIGHT| Maze height| HEIGHT=15
|ENTRY| Entry coordinates (x,y)|ENTRY=0,0
|EXIT| Exit coordinates (x,y)|EXIT=19,14
|OUTPUT_FILE| Output filename|OUTPUT_FILE=maze.txt
|PERFECT| Is the maze perfect?|PERFECT=True
|SEED| (Optional) Seed to use|SEED=42|
|DISPLAY| (Optional) Display for rendering|DISPLAY=ascii|
|ALGORITHM| (Optional) Algorithm to use|ALGORITHM=rb|

**Display** : `emoji` *(default)* | `ascii`\
**Algorithm**: `rb` *(default)* | `huntandkill`

---

## 🖥️ Interactive terminal

When you launch the project, the maze will be draw and a menu will appear at the bottom. Use the keyboard to choose whatever option you want:

|KEY|Name|Description|
|:-:|:--:|:---------:|
|1|Re-generate a new maze|Regenerate a new maze, with a new seed|
|2|Show/Hide path from entry to exit|Show or hide the shortest path from entry to exit|
|3|Rotate maze colors|Roatate randomly the maze walls color and, if youŕe lucky, the 42 pattern|
|4|Change algorithm|Show a sub-menu in which you can choose the algorithm you want to use for the next generation|
|5|Show seed|Show the seed used|
|6|Quit|Quit the menu and the program|

---

## 📂 Architecture overview:

- **a_maze_ing.py**: The main script of the project.
- **src/utils/**: utils functions for the A_Maze_Ing project.
- **src/maze/***: The reutilisable maze generation module.

### ✍ How all of this works?

The first thing to do is to check if the maze configurations is good. So in the **src/maze/maze_config.py**, the `MazeConfig` class check, with `pydantic` if the configuration gave by the user respect the standard *(no entry or exit outside the maze, entry and exit not and the same place, etc...)*.\
If evertyhing is good, then the `MazeConfig` object can be instancied and all the configurations will be stored inside a variable.

**src/maze/maze_fortytwo_pattern.py** create the 42 pattern at the middle of the maze. The coordinates are stored in a set so it's more easy to check in the future.

The core of the module is the **src/maze/maze_generator.py**. Inside, the class `MazeGenerator` contain the maze in `self.maze`. **The main function** `maze_generator()` print the text, generate a seed if needed, the maze, print it, check if it can be solved and create the output file.\

**src/maze/maze_solver.py** contain the `MazeSolver` class used to print the shortest path (if possible), and print it.

**src/maze/errors.py** contain custom errors relative for this project.

**src/maze/customization** is a list of **Enum Class** used to customize the maze and be more efficient than a simple `self.maze_wall` (and prevent having 800 lines in the maze_generator.py).

To have the file output, to print the maze and the solution inside a file, we've created it inside the **src/maze/output/maze_ouput.py**.

Finally, all the algorithms are in **src/maze/algorithms/**.

---
## 🔑 Public API

```python
from maze import MazeConfig, MazeGenerator, MazeSolver
```

- MazeConfig — base model class checking configuration and creating the config object.
- MazeGenerator — factory used to instantiate maze and print it.
- MazeSolver — class to check if a maze is solvable.

---

## 🚨 MazeGenerator

- Create unique maze based on a seed (can be reproduce).
- Seed is generated automatically if user doesn't provide it.
- Render the maze based on user choice.
- Solve the maze to provide a fully functionnal maze.
- Generated **perfect** and **imperfect** mazes.
- Generated walls around the maze to keep it simple.
- Provides multiples display and algorithms.

---

## 🌚 Quick example

```python
#!/usr/bin/env python3

from maze import MazeConfig, MazeGenerator, MazeSolver

# Generate the config object with custom parameters.
config = MazeConfig(width=50, height=50, entry=(0,0), exit=(18,12), output_file="maze.txt", perfect=False, display="emoji", algorithm="rb")

# Instanciate a new maze.
generator = MazeGenerator(config)

# Generate a new maze and display it.
generator.maze_generator(rendering=True)

# Display the maze parameters.
generator.get_maze_parameters()

# Create new config from file.
cool_config = MazeConfig.from_config_file("config.txt")

# Instanciate another maze and do not render it.
my_super_maze = MazeGenerator(cool_config)
my_super_maze.maze_generator(rendering=False)

# Solve a maze and print the result
solver = MazeSolver(my_super_maze)
solver.find_path()
solver.print_maze_solver()
```

---

## 🤖 Maze generation algorithm:
1. **Explanation**:

We choose two algorithms for this project.

The first one is the **Backtracking Algorithm**.
- First, it choose a random starting point in the maze and carve a path.
- Then, it choose a random unvisited neighbor and carve a path.
- It push the current cell to the stack/history.
- If there are no unvisited neighbors (dead end), pop from the stack to return to the previous cell.
- Finally, it continue until the algorithm returns to the starting point.

The second one is the **Hunt and Kill Algorithm**.
- It choose a random starting point in the maze and carve a path.
- If it reach a dead end, then it looks for the first cell that neighbors part of the maze. It check from the left, to the right starting the first line.

2. **Why we choose this**:

We choose those algorithms for two reasons. The first one is to train on the backtracking part. The second one is just for the visual. It looks good.

3. **Part of the code reusable, and how to do it**:

All the files in the `src/maze/` folder are a part of the package.

Install the package using `pip`
```bash
pip install ~/mazegen-1.0.0-py3-none-any.whl
```

Import the generator using
```python
from maze.maze_generator import MazeGenerator
```
In your code, you can use the `MazeGenerator()` function to generate a Maze and store it a variable.\
To import your configs, you can use two methods:\
- Using the `MazeConfig` import (`from maze.maze_config import MazeConfig`). Then:
```python
config = MazeConfig.from_config_file("config.txt")
```
Make sur that your config match the format above (or copy-paste the file in the repo).
- Alternatively, past your config directly in the function call:
```python
config = MazeConfig(width=50, height=50, entry=(0,0), exit=(18,12),output_file="maze.txt", perfect=False)
```
<br>

Then you can create your `MazeGenerator` object using:
```python
generator = MazeGenerator(config)
```
To generate the maze, use:
```python
generator.maze_generator(rendering=True)
```
- rendering: True to print the maze in the terminal.

<br>

Other functions:

You can print the maze parameters by using:
```python
print(generator.get_maze_parameters())
```

You can print the maze using:
```python
generator.print_maze()
```

<br>

The generator use the `MazeSolver` class itself to check if the Maze can be solved. You can import this package `from maze.maze_solver import MazeSolver` and use this function to create the `MazeSolver` object.
```python
solver = MazeSolver(generator)
```
Then, check if a path exist using:
```python
solver.find_path()
```
and print it using:
```python
solver.print_maze_solver()
```

---

## 🧑‍🏫 The Team:
1. Roles of each team member:

- roandrie: [norme corrector, readme writer, files organizer, writing customization and parsing]
- rruiz: [math pro, debugger, writing algorithms, docstring pro]

2. Anticipated planning, and the evolution:

There was not a planning at the start. I (roandrie) started the project before rruiz because he was still on the python modules. So I started the repo, the parsing, errors managements, creating everything we need. Then, we works and what we needed : creating the maze, filling it, creating the algorithm etc...

3. What worked well, what improvement could be done:

Our team was good. Nothing can be improved apart from our coding skill.

---

## 📂 Specific tools:

We use 2 differents libraries:
- `pydantic` to check if the config is correct.
- `colorama` to print the maze on the terminal and add colors and style in the text.

---

## 💿 Resources
#### <u>For Maze Algorithm</u>:
##### General:
- https://professor-l.github.io/mazes/
- https://www.youtube.com/watch?v=sVcB8vUFlmU
- https://en.wikipedia.org/wiki/Maze_generation_algorithm

##### Recursive Backtracking:
- https://inventwithpython.com/recursion/chapter11.html

##### Hunt and kill:
- https://weblog.jamisbuck.org/2011/1/24/maze-generation-hunt-and-kill-algorithm
- https://www.reddit.com/r/proceduralgeneration/comments/1f7w3u7/huntandkill_maze_algorithm/

<br>

#### <u>For Maze Solver</u>:
- https://medium.com/@msgold/using-python-to-create-and-solve-mazes-672285723c96
- https://en.wikipedia.org/wiki/Breadth-first_search
- https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
- https://medium.com/@luthfisauqi17_68455/artificial-intelligence-search-problem-solve-maze-using-breadth-first-search-bfs-algorithm-255139c6e1a3
- https://stackoverflow.com/questions/57201946/how-do-i-find-shortest-path-in-maze-with-bfs

<br>

#### <u>For Building Package</u>:
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

<br>

#### <u>AI Usage</u>:

AI was use to better understanding certain things in Python. And help us on some maths aspect. Also, help use optimize more part of code (because Python can be easy but also be very unclear at some part).

---
