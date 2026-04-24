*This project has been created as partof the 42 curriculum by roandrie*

---

## ✏️ Quick Start

```bash
make  # install all dependencies and run the script

uv sync  # alternatively you can also use this

uv run python -m src  # Launch with the default value
```
> [!NOTE]
> If you don't have `uv` installed, run `make install`

---

## 📂 Description

A **Large Language Model (LLM)** is an artificial intelligence system trained on massive datasets to process, understand, and generate human language. Technically, it operates as a probabilistic engine that calculates and predicts the most relevant next token based on the provided input context.

### About This Project: Function Calling & Constrained Decoding

Large Language Models (LLMs) excel at understanding natural language but lack the native ability to produce reliable, machine-executable outputs. This project focuses on **Function Calling**, a mechanism that translates user prompts into structured function calls (e.g., JSON formats with typed arguments) to interact with external systems, execute code, and extract data.

**The Technical Challenge:**
While large models can format outputs natively, smaller models (e.g., 0.6B parameters) are notoriously unreliable at generating valid data structures, often failing 70% of the time when prompted for JSON.

**Our Approach:**
To achieve production-grade reliability (99%+), this project implements **Constrained Decoding**. Rather than relying on prompt engineering, this technique controls the model's generation process token-by-token, mathematically guaranteeing a valid structural output.

### 📜 Summary:

This project focuses on building a function calling tool that translates natural language prompts into structured function calls. Given a specific user question *(e.g., "What is the sum of 40 and 2?")*, the system must not answer the question directly, but instead output the appropriate function name and its required arguments formatted as JSON:
```bash
[
	{
	"name": "fn_add_numbers",
	"description": "Add two numbers together and return their sum.",
	"parameters": {
		"a": {
			"type": "number"
		},
		"b": {
			"type": "number"
		}
	},
	"returns": {
		"type": "number"
	}
	}
]
```
The implementation relies on **constrained decoding** to guarantee 100% valid JSON output. This technique modifies the logits before token selection by setting the probabilities of schema-breaking tokens to negative infinity, ensuring reliable outputs even with a small 0.5B parameter model.

The system processes two main input files located in the `data/input/` directory:
* `function_calling_tests.json`: Contains the natural language prompts to evaluate.
* `function_definitions.json`: Defines the available functions, including argument names, types, and descriptions.

The program must generate a single output file named `function_calling_results.json`. Each object within this array must strictly contain the `prompt`, the function `name`, and the `parameters`. The final solution must achieve over 90% accuracy for function selection and process all test prompts in under 5 minutes.

### 📝 Rules:

- Must be written in **Python >=3.10**.
- Must adhere to the **flake8** and **mypy** standard.
- Crash and leaks must be properly managed. All errors must be handled gracefully.
- Code must include type hints and docstrings *[(following PEP 257)](https://peps.python.org/pep-0257/)*
- All classes must use `pydantic` for validation.
- `dspy` (or any similar package) is forbidden including `pytorch`, `huggingface package`, `transformers`, `outlines`, etc.
- The model we need to use for this project must be **Qwen/Qwen3-0.6B** by default. But any other models can be used as long the project works with the mandatory model.
- It's forbidden to use any private methods or attributes from the `llm_sdk` package.
- The function to call should be chosen using the LLM.

### 📮 Makefile:

This project must have a Makefile and the following rules:
- **install**: install project dependencies using **pip**, **uv** etc...
- **run**: execute the main script of the project.
- **debug**: run the main script in debug mode using Python's pdb.
- **clean**: Remove temporary files or caches.
- **lint**: execute the commands `flake8` . and `mypy . --warn-return-any
--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs
--check-untyped-defs`.
- **lint**: execute the commands `flake8 .` and `mypy . --strict`.

---

## 💡 Instructions

### 1. Git clone this repository:
```bash
git clone https://github.com/Overtekk/Call_me_Maybe.git
```

### 2. Install dependencies:
```bash
make  # install all dependencies and run the script

uv sync  # alternatively you can also use this
```
> [!NOTE]
> If you don't have `uv` installed, run `make install`

Using `uv run python -m src` (or `make run`) you will launch the program using the default argument.\
If you want to use your own files, use those flags

| FLAGS | DEFINITION |
|:-----:|:--------------:|
| -f / --functions_definition | path where function definition in json is stored |
-i / --input |  path where input file in json is stored |
 -o / --output |  path to the output file in json |

 You can also use two other flags:
 - **-v (--visualizer)**: to show the visual progress of the LLM.
 - **-d (--debug)**: to show the debug mode.
 - **-m (--model)**: to use another model (default is Qwen/Qwen3-0.6B)

 Usage:
 ```bash
 usage: python -m src [--functions_definition <function_definition_file>] [--input <input_file> [--output <output_file>]
 ```

---

### 🖱️ Support for other models

By using the flag **-m model_name** you can specify an other model from Hugging Face. Qwent is a low model langage so is performance are a bit bad. Other model are better trained so output can be different.

Example of use:
```bash
 uv run python -m src -v -m HuggingFaceTB/SmolLM2-360M
```
or
```bash
 uv run python -m src -v -m Qwen/Qwen2.5-1.5B
```

---

## ✍ Example of use:

**Input Example**:

```json
  {
    "prompt": "What is the square root of 16?"
  }
```

**Output Example**:
```json
  {
    "prompt": "What is the square root of 16?",
    "name": "fn_get_square_root",
    "parameters": {
      "a": 16.0
    }
  }
```

---

## ⚙️ How it works?

### Algorithm:

The core of this project relies on **Constrained Decoding** to force the LLM to output valid data. Instead of letting the model freely predict the next word, we intercept its "thought process" (the logits) at every single token:

1. Prompt Encoding: The user prompt and instructions are converted into token IDs.

2. Logit Calculation: The model evaluates the probability (logits) of all possible next tokens in its vocabulary.

3. Masking: We apply a mask of `-numpy.inf` to any token that breaks our desired schema. For example, when expecting a number, all alphabetical tokens are masked.

4. Selection: We use `numpy.argmax` to select the highest probability token among the allowed tokens.

5. Iteration: This token is appended to our sequence, and the loop repeats until the structural condition is met (e.g., a newline or the end of a valid number).

### Choice of design:

The architecture is built around Separation of Concerns and strict type validation:

- **Validation Layer** `(src/parser)`: Uses `pydantic` and `TypeAdapter` to rigorously validate input JSON schemas (`functions_definition.json` and `function_calling_tests.json`) before any LLM processing.
It create the `output` folder and file if they don't exist.

- **Engine Layer** `(src/engine)`: The `CallMeMaybe` class acts as the orchestrator. It separates the generation into two distinct phases: determining the function name, and then extracting the specific parameters.\
`llm_instructions_model` will be used to give instructions and context to the LLM.\
`prompt` will be used to store all promps and give it to the main class.
`Vocabulary` contains all vocabulary and logics used by the LLM.
`Output` will store results and write them in the output file.

- **Utilities** `(src/utils)`: A custom timing decorator (`func_timer`) using `perf_counter` ensures we can monitor performance to stay within the 5-minute execution limit.

### Performance analysis:

By restricting the LLM's vocabulary dynamically rather than relying on heavy, iterative self-correction prompts, the generation speed is significantly optimized. The model only generates the exact characters needed for the arguments (e.g., stopping early using a max_tokens limit of 42 for numbers or 100 for strings). This ensures the program handles the entire evaluation suite well under the maximum allowed timeframe.\
The negative value on that is that the LLM is not very "smart". It will choose the best functions among all on those yoou are available, but if a promps is ambiguous *(like "What is the essence of life")*. It will choose the best function, for him, that correspond to the promp. We can correct that by increasing the instructions and the generating phase, by adding more rules for example, but it's not the main focus of this subject.

The LLM have a auto-retry feature if a generation doesn't work. It will have a new prompt to try, and start the generation again.

### Challenges faced:

**Understanding the subject**. It was very, very, very difficult to know what to do after the parsing. Thanks to some of my peers, I managed to understand the project after a bit of strugling.

**Prompt Collapse**: Small models (like Qwen 0.6B) struggle with long lists of negative constraints ("Do not calculate", "Do not change case"). The solution was to transition to structured the context and give only the thing that was necessary to him.

**Traps**: When giving empty string, max int value, and other things like that, the LLM was collapsing, crashing or enter an infinite loop. The solution was to limit the number of try the LLM can do before stopping the generation.

### Testing strategy:

**Function Calling Accuracy**: Injecting edge-case prompts such as extremely large numbers (999999999999999.99), negative floats (-0.0000001), empty strings (''), and complex punctuation to ensure the extraction engine works. It do not give the best answer, but it works.

**Robustness & Error Handling**: Manually corrupting the input JSON files, providing non-existent model paths, and passing empty prompts to confirm the program safely catches exceptions and prints coherent error messages using the Rich library instead of crashing with native stack traces.

## 🖱️ Comprehensive test suite

### Run
```bash
make tester
or
uv run python -m unittest discover -s tests
```

This will launch the test suite to test some functions and methods. It will only test if a json input in valid, or not.
It's not completed because I juste wanted to test it and didn´t know what tests to do.

---

## 📚 Resources

### Documentation for the `Rich` library
| Resource | Description |
| :------: | :---------: |
| [Rich docs ‒ Official Documentation](https://rich.readthedocs.io/en/stable/) | Using the `rich` library to format the text using colors, style etc... |

### Documentation for the `argparse` library
| Resource | Description |
| :------: | :---------: |
| [Docs Python ‒ argparse documentation](https://docs.python.org/3/library/argparse.html) | Using specific things with argparse |

### Documentation for the `pydantic` library
| Resource | Description |
| :------: | :---------: |
| [Docs Pydantic ‒ Type Adapter](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) | Use **type adapters** to perform better validation |

### Constrained Decoding:
| Resource | Description |
| :------: | :---------: |
| [Aidencooper ‒ Constrained Decoding](https://www.aidancooper.co.uk/constrained-decoding/) | Guide to understand what is constrained decoding and how to do it |

### Other documentation, useful links and references
| Resource | Description |
| :------: | :---------: |
| [Github of **shadox254**](https://github.com/shadox254/Call-Me-Maybe) | Help building my project and understand what to do
| [Github of **69Nesta**](https://github.com/69Nesta/42-Call-Me-Maybe) | Same as above
| [Github of **alizealebaron**](https://github.com/alizealebaron/call_me_maybe/tree/main) | Same as above
| [py.typed](https://safjan.com/the-importance-of-adding-py-typed-file-to-your-typed-package/) | Correcting lint error from the llm_sdk |

### IA was use to:
- **As a supervisor** ‒ this subject is a bit complexe and not very clear. I'm was lost after the parsing and didn't know what to do (even after searching on github). So I use IA to help me, explaim what I was supposed to do, how to do that. But I make sure that I understand and that it did not give code.
- **Help writing docstrigs** ‒ ensure that the docstrings is clear and short. I writes something and give it to have a better writing style than me because docstrings is important.
- **Help improving the prompt** - enhance my previous prompt to remove what was unclear, and go directly to the topic.
- **Refactoring** - help to refactor my code and learn how to write better code.
- **Optmization** - help to optimize part of my code (like create the toquence sequence only once, and not for each prompts)
- **Help with bug** - when I had some bugs and didn't know how to fix, I ask AI to help me like a teacher.

---



