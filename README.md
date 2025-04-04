---

# R.A.P.L. (Rapid Application Programming Language)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Example Code](#example-code)
4. [Showcase](#showcase)
5. [Command Descriptions](#command-descriptions)
6. [Usage](#usage)
7. [Contributing](#contributing)

---

## Introduction

**R.A.P.L.** (Rapid Application Programming Language) is a developing programming language designed for simplicity and efficiency. It aims to make coding more intuitive by providing a clean syntax for logic, loops, and function handling.

---

## Installation

Requirements to run the program:
- [Python](https://www.python.org/downloads/) [Recommended: v3.12.6]
- [git](https://git-scm.com/downloads) [Recommended: v2.48.1]

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RAYANEPROGRAMMER/RAPL.git
   ```

2. **Run the R.A.P.L. shell**:
   ```bash
   python shell.py
   ```

---

## Example Code

Here is a sample R.A.P.L. program that showcases function definitions, loops, and string manipulations:

```rapl
# This is a very useful piece of software

def oopify(prefix) -> prefix + "oop"

def join(elements, separator)
	let result = ""
	let len = len(elements)

	for i = 0 to len then
		let result = result + elements/i
		if i != len - 1 then let result = result + separator
	end

	return result
end

def map(elements, func)
	let new_elements = []

	for i = 0 to len(elements) then
		append(new_elements, func(elements/i))
	end

	return new_elements
end

print("Greetings universe!")

for i = 0 to 5 then
	print(join(map(["l", "sp"], oopify), ", "))
end
```

This program:

- Adds `"oop"` to each string element.
- Joins a list of strings with a separator.
- Applies a function to each element of a list.
- Prints the modified list multiple times.

Basic Hello world program:

```rapl
let message = "Hello World!"

print(message)
```

This program:

- Print 'Hello world' to the terminal.

---

## Showcase

This is a screenshot from inside VSCode of the example code:

![VSCode Screenshot](Screenshots/Example_code_vscode)

The syntax highlighting is part of an extension that is still under development and not ready for release.

---

## Command Descriptions

For a full list of commands, refer to the [Commands](Commands.md) file in the repository. Below are some key commands:

- **let**: Defines a non-constant variable.
- **def**: Declares a function.
- **for/while**: Loops through code blocks.
- **if/elif/else**: Conditional logic.
- **return**: Exits a function with an optional return value.

For the complete list and detailed descriptions, check the `Commands.md` file in the repository.

---

## Usage

To run a R.A.P.L. program, follow these steps:

1. Write your R.A.P.L. code in a file with the `.rapl` extension (e.g., `program.rapl`).

2. Run the **R.A.P.L. shell**:
   ```bash
   python shell.py
   ```

3. Inside the R.A.P.L. shell, run your program with:
   ```rapl
   run("program.rapl")
   ```

**Note:**  
Paths such as `C:\Users\pc\Desktop\example_HelloWorld.rapl` won't work; instead, use `C:/Users/pc/Desktop/example_HelloWorld.rapl`.  
This occurs because the program doesn't handle the `\` character; instead use `/`.

This will execute your R.A.P.L. program within the custom shell.

---

## Contributing

R.A.P.L. is still in development. Contributions, bug reports, and suggestions are welcome! To contribute:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

---

## Authors

- **Rayan Berrabah** -
  [Github](https://github.com/rayvn-42)

---

## License

This project is licensed under the [MIT](LICENSE) License - see the [LICENSE](LICENSE) file for details
