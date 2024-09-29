---

## R.A.P.L. (Rapid Application Programming Language)

### Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Example Code](#example-code)
4. [Showcase](#showcase)
5. [Command Descriptions](#command-descriptions)
6. [Usage](#usage)
7. [Contributing](#contributing)

---

### Introduction

**R.A.P.L.** (Rapid Application Programming Language) is a developing programming language designed for simplicity and efficiency. It aims to make coding more intuitive by providing a clean syntax for logic, loops, and function handling.

---

### Installation

To set up R.A.P.L. and get started:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/rapl.git
   ```

2. **Run the R.A.P.L. shell**:
   ```bash
   python shell.py
   ```

---

### Example Code

Here is a sample R.A.P.L. program that showcases function definitions, loops, and string manipulations:

```rapl
# This is a very useful piece of software

FUNC oopify(prefix) -> prefix + "oop"

FUNC join(elements, separator)
	DEF result = ""
	DEF len = LEN(elements)

	FOR i = 0 TO len THEN
		DEF result = result + elements/i
		IF i != len - 1 THEN DEF result = result + separator
	END

	RETURN result
END

FUNC map(elements, func)
	DEF new_elements = []

	FOR i = 0 TO LEN(elements) THEN
		APPEND(new_elements, func(elements/i))
	END

	RETURN new_elements
END

PRINT("Greetings universe!")

FOR i = 0 TO 5 THEN
	PRINT(join(map(["l", "sp"], oopify), ", "))
END
```

This program:

- Adds `"oop"` to each string element.
- Joins a list of strings with a separator.
- Applies a function to each element of a list.
- Prints the modified list multiple times.

---

### Showcase

This is a screenshot from inside VSCode of the example code. The syntax highlighting is part of an extension that is still under development and not ready for release:
![VSCode Screenshot](Screenshots/Example_code_vscode)

---

### Command Descriptions

For a full list of commands, refer to the `Commands.md` file in the repository. Below are some key commands:

- **DEF**: Defines a non-constant variable.
- **FUNC**: Declares a function.
- **FOR/WHILE**: Loops through code blocks.
- **IF/ELIF/ELSE**: Conditional logic.
- **RETURN**: Exits a function with an optional return value.

For the complete list and detailed descriptions, check the `Commands.md` file in the repository.

---

### Usage

To run a R.A.P.L. program, follow these steps:

1. Write your R.A.P.L. code in a file with the `.rapl` extension (e.g., `program.rapl`).

2. Run the **R.A.P.L. shell**:
   ```bash
   python shell.py
   ```

3. Inside the R.A.P.L. shell, run your program with:
   ```rapl
   RUN("program.rapl")
   ```

**Note:**  
Paths such as `C:\Users\pc\Desktop\example_HelloWorld.rapl` won't work; instead, use `C:/Users/pc/Desktop/example_HelloWorld.rapl`.  
This occurs because the program doesn't handle the `\` character; instead, we use `/`.

This will execute your R.A.P.L. program within the custom shell.

---

### Contributing

R.A.P.L. is still in development. Contributions, bug reports, and suggestions are welcome! To contribute:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

---
