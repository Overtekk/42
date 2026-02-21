 *This project has been created as part of the 42 curriculum by roandrie"

---


## ✏️ Quick Start

### Compile the project:
```bash
make
```

### Run manually:
```bash
./codexion <number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor> <number_of_compiles_required> <dongle_cooldown> <scheduler>
```

#### Using the Tester Script:
A tester.sh script is provided to run predefined scenarios.
```bash
./tester.sh <test_id> [mem]
```
- `test_id`: Can be a number (1 to 6) or specific case names like `starvation2`, `large_edf`, `one_compiler_edf`, `big`.
- `mem` (optional): Runs the test with Valgrind to check for memory leaks.

*Example:* `./tester.sh starvation2 mem`

---
<br>

## 📂 Description
### 📜 Summary:
The goal is to create a competition between differents coders using **thread**.\
There is one or more **coders**. Each can do 3 things at a time:
- **compile**
- **debug**
- **refactor**

They compile, then debug, then refactory and start compile right after finishint refactoring.\
Coders can **burns out** starting the simulation or when they finish compiling. They need to compile before the timer hits 0.\
Do to that, they need **USB dongles**. They are many dongles that coders. To compile, they need a dongle in each hands. Once compiling is done, they start debugging, then they start refactoring.\
If each coders have compiled a certain amount of time, the simulation can stop.\
They can't communicate and they do not know when a coder will burns out.

It's a compilation because codes are in a circular hub. So, **Coder 1** sit next to **Coder 2** and **Coder 4** (assuming they are 4).\
They are **4 USB dongles**.

Here a diagram to better understanding:

```bash
					CODER 1
					(Compile)
					/		\
			Dongle D		Dongle A
		(Taken by 1)		(Taken by 1)
			 /					   \
		  CODER 4				  CODER 2
	(Wait Dongle D)        	   (Wait Dongle A)
			\                     /
		  Dongle C            Dongle B
		(Taken by 4)     	(Taken by 2)
					\       /
					 CODER 3
					  (Wait)
```

### 📝 Rules:

- Each coder need to be represented by a **thread** (using `pthread_create`).
- If there is **1 coder**, it will **burns out** since there is only **1 USB dongle**.
- To prevent coders from duplicating dongles, **dongle's state must be protected** with a **mutex** (`pthread_mutex_t`). A condition variable (`pthread_cond_t`) may be
used to manage waiting queues.
- There is a **scheduler** to manage priority:
- **FIFO**: First In, First Out. Follow the queue to give dongles.
- **EDF**: Earliest Deadline First. The coder that will burn out first will take the dongles.
- The program must guarantee liveness. So coders should not burns out under edf scheduling, provided the parameters are feasible.
- A separate **monitor** thread must detect burnout precisely and stop the simulation.
The burnout log must be printed **within 10 ms** of the actual burnout time.
- Logging must be **serialized** so that two messages never interleave on a single line (use a **mutex** to protect output).
- Code must compile with **-Wall -Wextra -Werror -pthread**.
- A priority queue **(heap)** for **FIFO**/**EDF** scheduling must be implemented.
- No memory leaks.
- Global variables are forbidden.
- Logs must follows rules (see below).
- Those arguments are mandatory:

|Arguments|Value|Description|
|:-------:|:---:|:---------:|
|number_of_coders|>=1|Number of coders ans also the number of donglers|
|time_to_burnout|>=1|(in ms)Time before a coder will burns out since the last compilation. Start at the beginning of the simulation|
|time_to_compile|>=1|Time it takes for a coder to compile. During that time, it need to hold two dongles|
|time_to_debug|>=1|Time a coder spend debugging|
|time_to_refactor|>=1|Time a coder will spend refactoring. After completing this phase, it will immediately attempts to acquire dongles and start compiling again|
|number_of_compiles_required|>=1|If all coders have compiled at least this many times, the simulation stops||
|dongle_cooldown|>=1|Time before a dongle can be used again||
|scheduler|`fifo` or `edf`|The arbitratin policy used by dongles||

<br>

### 📮 Makefile:

Makefile need to have those rules:
- **NAME** variable
- all
- clean
- fclean
- re

It must not relink.

<br>

### 🏷️ Authorized Functions:

|Thread managements|Mutex|Thread cond|Memory management|Printing|Other|
|:----------------:|:---:|:----------:|:--------------:|:------:|:---:|
|pthread_create|pthread_mutex_init|pthread_cond_init|malloc|write|gettimeofday|
|pthread_join|pthread_mutex_lock|pthread_cond_wait|free|fprintf|usleep|
||pthread_mutex_unlock|pthread_cond_timedwait|memset|printf|strcmp|
||pthread_mutex_destroy|pthread_cond_broadcast|||strlen|
|||pthread_cond_destroy|||atoi|

<br>

### 💻 Logs:

Any state change of a coder must be formatted as follows:
```bash
- timestamp_in_ms X has taken a dongle
- timestamp_in_ms X is compiling
- timestamp_in_ms X is debugging
- timestamp_in_ms X is refactoring
- timestamp_in_ms X burned out
```

*X will be the coder number*

Rules:
- A displayed state message should not be mixed up with another message.
- A message announcing that a coder burned out should be displayed no more than 10 ms after the actual burnout.

---

## 💡 Instructions

### 1. Compile the project:
```bash
make
```

### 2. Run manually:
```bash
./codexion <number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor> <number_of_compiles_required> <dongle_cooldown> <scheduler>
```

### Or Use the Tester Script:
A tester.sh script is provided to run predefined scenarios.
```bash
./tester.sh <test_id> [mem]
```
- `test_id`: Can be a number (1 to 6) or specific case names like `starvation2`, `large_edf`, `one_compiler_edf`, `big`.
- `mem` (optional): Runs the test with Valgrind to check for memory leaks.

*Example:* `./tester.sh starvation2 mem`

|ID|Summary|
|--|:-----:|
|1|Basic test with 'fifo' scheduler|
|2|Basic test with 'edf' scheduler|
|3|Test that will success under 'fifo' scheduler|
|4|Test that will success under 'edf' scheduler (20 coders)|
|5|Test with a very low cooldown|
|6|Test with very long actions|
|big|Test with 100 coders and quick cooldown|
|starvation|Large burnout timer but compiling is at 600|
|starvation2|Same that 'starvation' but with 'edf' scheduler|
|one_compiler_fifo|Test with only one compiler|
|one_compiler_edf|Test with only one compiler|
|zero_compile|Test with zero compilation requiered|
|immediate_burnout|Test with a burnout to 1|
|cooldown_hell|Test with a big cooldown for dongle|
|max_coders|Test with 300 coders (max)|
|toomany_compiler|Test with too many compilers|
|error_arg<1-10>|Many test to test each arguments (goes to 1 from 10)|

---

## 🌟 What is a thread?

A **thread** is a lightweight unit of execution that enables multiple tasks to run simultaneously within a single process. Unlike standard sequential execution, threads operate in parallel while sharing the same memory space. This shared memory allows for rapid data exchange but requires careful synchronization (using Mutexes) to avoid data corruption. In C, the `<pthread.h>` library is essential for this project to simulate independent actors performing real-time actions without blocking the main program's execution.

---

## 🐨 How it works?

1. **Initialization**: The main process allocates memory, initializes mutexes for shared variables and dongles, and creates the priority structures (Queue for FIFO, Min-Heap for EDF).
2. **Execution**: Each coder is launched as an independent thread (`pthread_create`). They enter an infinite loop of computing phases: waiting for scheduler approval, taking dongles, compiling, debugging, and refactoring.
3. **Scheduling Policy**: Before taking dongles, a coder must be authorized by the scheduler. EDF uses a "local priority" system where a coder yields if its immediate neighbors have a more urgent burnout deadline.
4. **Monitoring & Cleanup**: A detached monitor thread continuously checks the timestamp of each coder's last compiling. If `time_to_burnout` is exceeded, the monitor flags the simulation as stopped, broadcasts a signal to wake up all sleeping threads, and allows the main process to join threads and free all allocated memory cleanly.

<br>

I used Min-Heap for EDF because the subject requiered it but also because it's more easy to implement this type of priority queue. Comparison are simple and move a coder too.
For the FIFO, I used a simple linked list because the first to go in will the... the first one, and go one. It was more easy to build it that way either for managing thread, either for building the functions.

---
<br>

## 🛸 Blocking cases handled

Concurrency introduces several critical issues that must be addressed to guarantee the liveness of the simulation.

- **Deadlock Prevention & Coffman's Conditions**: Deadlocks occur when circular wait conditions are met. This is prevented through an asymmetric allocation strategy. The last coder in the circle attempts to take the right dongle before the left one, breaking the circular wait. Additionally, the `take_dongle` function uses a fallback mechanism: if the first dongle is acquired but the second is locked, the thread releases the first dongle and yields, preventing it from holding resources indefinitely while waiting.
- **Starvation Prevention**:
  - In **FIFO**, a strict linked-list queue ensure coders access dongles in the exact order they requested them.
  - In **EDF**, a local priority evaluation is implemented. A coder only waits if its immediate left or right neighbor has an earlier deadline. This allows maximum parallelism across the table while guaranteeing that the most urgent local nodes are served first.
- **Cooldown Handling**: Dongles are treated as entities with their own cooldown timestamps. Before a dongle can be locked by a new coder, the scheduler verifies that `current_time >= last_used_time + cooldown`.
- **Precise Burnout Detection**: The monitoring thread operates independently, itrating through the coders array with a micro-sleep (`usleep`). It only locks the specific `mutex_burnout` of the coder being checked. This allows detecting a burnout and printing the log within the strict <10ms requirement.
- **Log Serialization**: Standard output is not thread-safe. A global `mutex_print` is used to encapsulate every logging action, ensuring that timestamps and messages never interleave on the terminal.

---
<br>

## 🕛 Thread synchronization mechanisms

The simulation relies heavily on POSIX threading primitives to coordinate access to shared resources and ensure thread-safe communication.

- **`pthread_mutex_t`**:
  - **Resource Locking**: Each USB dongle has a dedicated mutex. It acts as a physical lock; a thread must acquire the mutexes of both its assigned dongles to start compiling.
  - **Data Race Prevention**: Shared variables like `simulation_active`, `time_to_burnout`, and `have_finished` are protected by individual mutexes. When the monitor reads a coder's state, it locks `mutex_burnout` just long enough to copy the value, preventing a data race if the coder updates its timestamp simultaneously.
- **`pthread_cond_t`**:
  - Used heavily in the schedulers to avoid CPU-intensive busy-waiting (polling). When a coder is added to the waiting queue (FIFO) or the Heap (EDF) and cannot proceed, it calls `pthread_cond_wait`. This puts the thread to sleep (0% CPU usage).
  - When a coder finishes compiling and releases its dongles, it triggers a `pthread_cond_broadcast`. This sends a wake-up signal to all sleeping threads, allowing them to re-evaluate their priority and attempt to acquire the dongles again. This mechanism is also crucial during a burnout event to wake up all blocked threads and terminate the process without memory leaks.

---
<br>

## 📚 Resources

### Threads:
- https://www.geeksforgeeks.org/c/thread-functions-in-c-c/
- https://www.codequoi.com/threads-mutex-et-programmation-concurrente-en-c/

#### Queue:
- https://medium.com/@chedy.smaoui/coding-basics-thread-safe-blocking-queue-in-c-6ecad9b4980a
- https://stackoverflow.com/questions/8253278/message-passing-between-threads-in-c
- https://stackoverflow.com/questions/10721148/how-to-implement-thread-safe-queues
- https://sites.uclouvain.be/SyllabusC/notes/Theorie/Threads/threads2.html

#### Min-Heap:
- https://www.geeksforgeeks.org/dsa/introduction-to-min-heap-data-structure/
- https://www.geeksforgeeks.org/c/c-program-to-implement-min-heap/
- https://www.w3resource.com/c-programming-exercises/heap/c-heap-exercises-3.php
- https://en.wikipedia.org/wiki/Min-max_heap


<br>

### Man pages for functions
- https://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread_mutex_init.html

---
