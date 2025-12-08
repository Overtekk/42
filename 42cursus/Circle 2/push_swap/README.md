*This project has been created as part of the 42 curriculum by <roandrie>.*

### 📂 Description

The goal of this project is to sort a random list of integers using two stacks, **Stack A** and **Stack B**, and a **limited set of instructions**. It serves as a deep dive into **algorithmic complexity** and **data structures**.

Unlike standard sorting problems where you can swap any values, here we are constrained by the game rules. We can only manipulate the top of the stacks, push elements between them, or rotate the stacks. The challenge is to sort with the **minimum number of operations** possible:\
#### For 100% ->
* **100 numbers:** less than 700 moves.
* **500 numbers:** less than 5500 moves.

### 📊 Operations we can use:
**sa (swap a):** Swap the first 2 elements at the top of stack a.\
&emsp;Do nothing if there is only one element or none.\
****sb (swap b):** Swap the first 2 elements at the top of stack b.\
&emsp;Do nothing if there is only one element or none.\
**ss** : sa and sb at the same time.\
**pa (push a):** Take the first element at the top of b and put it at the top of a.\
&emsp;Do nothing if b is empty.\
**pb (push b):** Take the first element at the top of a and put it at the top of b.\
&emsp;Do nothing if a is empty.\
**ra (rotate a):** Shift up all elements of stack a by 1.\
&emsp;The first element becomes the last one.\
**rb (rotate b):** Shift up all elements of stack b by 1.\
&emsp;The first element becomes the last one.\
**rr :** ra and rb at the same time.\
**rra (reverse rotate a):** Shift down all elements of stack a by 1.\
&emsp;The last element becomes the first one.\
**rrb (reverse rotate b):** Shift down all elements of stack b by 1.\
&emsp;The last element becomes the first one.\
**rrr :** rra and rrb at the same time.

### 📦 **Library Integration:**
We are allowed to use our `libft` (especially linked lists or standard helper functions). However, the core logic relies entirely on the custom sorting algorithm we design.

## Instructions

### 🧙‍♂️ Compilation
To compile the project, clone [the repository](https://github.com/Overtekk/push_swap) and run `make`:

```bash
git clone https://github.com/Overtekk/push_swap
cd push_swap
make
```

### Run the program using:
```bash
./push_swap -4 7 +2 9 1
```
or
```bash
./push_swap "4752 1 -85 3 +21"
```

## I explain what I do below:

### 1. Parsing and Error Management
First, the program parses the arguments to ensure validity. It handles both single string input (`"./push_swap '1 2 3'"`) and multiple arguments (`./push_swap 1 2 3`). It checks for:
- Non-numeric characters.
- Duplicates.
- Integer overflow/underflow.

### 2. Sorting Small Stacks (3 numbers)
For a stack of 3 numbers, there are only 5 possible permutation cases (since the sorted case is already handled).
- I find the highest number.
- Depending on its position and the position of the other numbers, I execute a single combination of `swap` and `rotate` operations to sort the stack instantly (hardcoded logic for efficiency).

### 3. Sorting Medium Stacks (5 numbers)
- I push the two first numbers from **Stack A** to **Stack B**.
- I sort the remaining 3 numbers in **Stack A** using the algorithm described above.
- Then, I push the two numbers back from **Stack B** to **Stack A**, ensuring they land in the correct position.

### 4. The Main Algorithm (Large Stacks)
For larger sets of numbers, I use a **Cost-based Greedy Algorithm** (often referred to as the "Turk Algorithm" *(sources below)*). The logic is divided into two phases:

### Phase 1: A to B (Pushing Phase)
I push elements from **Stack A** to **Stack B** until only 3 elements remain in A. However, I don't push randomly:
- For every number in A, I calculate its "target" position in B. It means, its closest number. In 7 / 10 / 98 / -40 for **Stack A** and 58 / 3 / 23 for **Stack B**. Closest number for **7 is 3**, for **10 > 3** / **98 > 58** and **-40 > 3**.
- I calculate exactly how many operations (`ra`, `rb`, `rr`, `rra`, `rrb`, `rrr`) are needed to move each number to its target.
- I find the "median" is the list (1 for upper, 0 for below) to know if I execute `rr`/`rrr`.
- I select the "cheapest" node (the one requiring the fewest moves), execute the optimal rotation combination (optimizing with double rotations `rr`/`rrr` where possible), and push it to B.

### Phase 2: B to A (Return Phase)
Once **Stack A** has only 3 sorted elements:
- I use the **3 numbers sorting stack algorithm** in **Stack A**.
- I iterate through **Stack B**.
- For each element, I find its **Target Node** in **Stack A** (the smallest number in A that is larger than the element B).
- I rotate **Stack A** to bring this target to the top.
- I push the element from B to A.

### Final Step: Alignment
Finally, I rotate **Stack A** one last time to bring the smallest number (minimum) to the top of the stack, completing the sort.

## 📃 **Resources:**

#### https://medium.com/@ayogun/push-swap-c1f5d2d41e97
#### https://pure-forest.medium.com/push-swap-turk-algorithm-explained-in-6-steps-4c6650a458c0
#### https://www.youtube.com/watch?v=wRvipSG4Mmk
---
