
# Python Learning Guide

**Table of Contents:**
- [Python Learning Guide](#python-learning-guide)
  - [Introduction](#introduction)
    - [How Python code is executed](#how-python-code-is-executed)
    - [Difference between Compiler and Interpreter](#difference-between-compiler-and-interpreter)
    - [Difference Between Python and C++](#difference-between-python-and-c)
  - [Variables](#variables)
  - [Data Types](#data-types)
    - [Data Type: Code Examples:](#data-type-code-examples)
  - [Type Casting](#type-casting)
    - [A. Implicit Casting](#a-implicit-casting)
    - [B. Explicit Casting](#b-explicit-casting)
    - [C. Integer Conversion (`int()`)](#c-integer-conversion-int)
    - [D. Base Conversion with `int()`](#d-base-conversion-with-int)
    - [E. Floating-Point Conversion (`float()`)](#e-floating-point-conversion-float)
    - [F. String Conversion (`str()`)](#f-string-conversion-str)
    - [G. Sequence Conversion (`list()` / `tuple()`)](#g-sequence-conversion-list--tuple)
    - [H. Data Conversion Functions](#h-data-conversion-functions)
    - [I. Dunder Methods (Double Underscore)](#i-dunder-methods-double-underscore)
      - [Code Example: A "Price" Object](#code-example-a-price-object)
  - [Unicode System](#unicode-system)
    - [A. The Unicode Standard](#a-the-unicode-standard)
    - [B. Character Encoding (UTF-8)](#b-character-encoding-utf-8)
    - [C. String Encoding (`str` to `bytes`)](#c-string-encoding-str-to-bytes)
    - [D. String Decoding (`bytes` to `str`)](#d-string-decoding-bytes-to-str)
    - [E. Unicode Escape Sequences](#e-unicode-escape-sequences)
    - [F. Summary Table for Revision](#f-summary-table-for-revision)
    - [G. Understanding UTF (Unicode Transformation Format)](#g-understanding-utf-unicode-transformation-format)
      - [1. The Three Types of UTF](#1-the-three-types-of-utf)
      - [2. UTF-8 (The Industry Standard)](#2-utf-8-the-industry-standard)
      - [3. UTF-16 (The Middle Ground)](#3-utf-16-the-middle-ground)
      - [4. UTF-32 (The Fixed-Width Option)](#4-utf-32-the-fixed-width-option)
  - [Operators](#operators)
    - [A. Arithmetic Operators](#a-arithmetic-operators)
    - [B. Comparison (Relational) Operators](#b-comparison-relational-operators)
    - [C. Assignment Operators](#c-assignment-operators)
    - [D. Bitwise Operators](#d-bitwise-operators)
    - [E. Logical Operators](#e-logical-operators)
    - [F. Membership Operators](#f-membership-operators)
    - [G. Identity Operators](#g-identity-operators)
    - [H. Operator Precedence (Highest to Lowest)](#h-operator-precedence-highest-to-lowest)
    - [I. Membership Operators](#i-membership-operators)
      - [1. The `in` Operator](#1-the-in-operator)
      - [2. The `not in` Operator](#2-the-not-in-operator)
      - [3. Usage with Sequences (Lists \& Tuples)](#3-usage-with-sequences-lists--tuples)
      - [4. Usage with Sets](#4-usage-with-sets)
      - [5. Usage with Dictionaries](#5-usage-with-dictionaries)
    - [J. Identity Operators](#j-identity-operators)
      - [1. The `is` Operator](#1-the-is-operator)
      - [2. The `is not` Operator](#2-the-is-not-operator)
      - [3. The `id()` Function](#3-the-id-function)
      - [4. Key Takeaway: Identity (`is`) vs. Equality (`==`)](#4-key-takeaway-identity-is-vs-equality-)
  - [Comments](#comments)
    - [A. Single-Line Comments](#a-single-line-comments)
    - [B. Multi-Line Comments (Consecutive)](#b-multi-line-comments-consecutive)
    - [C. Multi-Line Comments (Triple Quotes)](#c-multi-line-comments-triple-quotes)
    - [D. Docstrings (Documentation Strings)](#d-docstrings-documentation-strings)
    - [E. Accessing Documentation](#e-accessing-documentation)
  - [Input \& Output](#input--output)
    - [A. The `input()` Function](#a-the-input-function)
    - [B. Type Casting with Type Hinting](#b-type-casting-with-type-hinting)
    - [C. Modern Formatting: F-Strings](#c-modern-formatting-f-strings)
    - [D. Advanced `print()` Control](#d-advanced-print-control)
    - [E. Practical Example: Area Calculator](#e-practical-example-area-calculator)
  - [Control Flow](#control-flow)
    - [A. Sequential Execution](#a-sequential-execution)
    - [B. Decision Making: `if-elif-else`](#b-decision-making-if-elif-else)
    - [C. Iteration: `for` Loop](#c-iteration-for-loop)
    - [D. Iteration: `while` Loop](#d-iteration-while-loop)
    - [E. Loop Control: `break`, `continue`, and `pass`](#e-loop-control-break-continue-and-pass)
    - [F. Loop with `else` Clause](#f-loop-with-else-clause)
    - [G. Nested Control Flow](#g-nested-control-flow)
    - [H. Modern Best Practice](#h-modern-best-practice)
  - [Functions](#functions)
    - [A. Types of Python Functions](#a-types-of-python-functions)
    - [B. Defining and Calling a Function](#b-defining-and-calling-a-function)
    - [C. Pass by Reference vs. Value](#c-pass-by-reference-vs-value)
    - [D. Types of Function Arguments](#d-types-of-function-arguments)
      - [1. Positional (Required) Arguments](#1-positional-required-arguments)
      - [2. Keyword Arguments](#2-keyword-arguments)
      - [3. Default Arguments](#3-default-arguments)
      - [4. Positional-Only Arguments (`/`)](#4-positional-only-arguments-)
      - [5. Keyword-Only Arguments (`*`)](#5-keyword-only-arguments-)
      - [6. Arbitrary (Variable-Length) Arguments (`*args`)](#6-arbitrary-variable-length-arguments-args)
    - [E. Order of Python Function Arguments](#e-order-of-python-function-arguments)
    - [F. Return Values](#f-return-values)
    - [G. Anonymous Functions (`lambda`)](#g-anonymous-functions-lambda)
    - [H. Variable Scope](#h-variable-scope)
    - [I. Default Arguments](#i-default-arguments)
      - [A. Basic Usage](#a-basic-usage)
      - [B. Combining with Positional Arguments](#b-combining-with-positional-arguments)
      - [C. The "Mutable Default Argument" Trap](#c-the-mutable-default-argument-trap)
    - [J. Keyword Arguments](#j-keyword-arguments)
      - [A. Basic Usage](#a-basic-usage-1)
      - [B. Independence of Order](#b-independence-of-order)
      - [C. Mixed Calling \& The Positional Rule](#c-mixed-calling--the-positional-rule)
    - [K. Positional Arguments](#k-positional-arguments)
      - [A. Key Rules for Positional Arguments](#a-key-rules-for-positional-arguments)
      - [B. Basic Usage (Correct Mapping)](#b-basic-usage-correct-mapping)
      - [C. Common Errors with Positional Arguments](#c-common-errors-with-positional-arguments)
      - [D. Positional vs. Keyword Arguments](#d-positional-vs-keyword-arguments)
    - [L. Arbitrary Arguments (`*args` and `kwargs`)](#l-arbitrary-arguments-args-and-kwargs)
      - [A. Arbitrary Positional Arguments (`*args`)](#a-arbitrary-positional-arguments-args)
      - [B. Arbitrary Keyword Arguments (`kwargs`)](#b-arbitrary-keyword-arguments-kwargs)
      - [C. The Golden Rule of Argument Order](#c-the-golden-rule-of-argument-order)
  - [Variable Scope](#variable-scope)
    - [A. Modifying Global Variables (`global`)](#a-modifying-global-variables-global)
      - [B. Modifying Nonlocal Variables (`nonlocal`)](#b-modifying-nonlocal-variables-nonlocal)
  - [Namespaces](#namespaces)
      - [Types of Namespaces:](#types-of-namespaces)
      - [A. The `globals()` and `locals()` Functions](#a-the-globals-and-locals-functions)
  - [Function Annotations](#function-annotations)
    - [A. Syntax and Usage](#a-syntax-and-usage)
    - [B. Accessing Annotations](#b-accessing-annotations)
    - [C. Annotations with Default Values](#c-annotations-with-default-values)


## Introduction

Guido van Rossum created Python as an
- **Interpreted language** - The code is executed line by line in real time 
- **Object-oriented language** - A programming style that organises code into reusable "objects" containing both data (attributes) and actions (methods)
- **Dynamically Typed:** The language determines the data types of a variable at runtime based on its value, rather than requiring an explicit declaration.
- **Garbage Collected:** An automatic memory management process that identifies and deletes data no longer being used by the program to free up space. 
- **Case-sensitive programming language**: That means "luffy" and "Luffy" are two different identifiers in Python.

### How Python code is executed

- **Source Code:** You write your instructions in a `.py` file using human-readable English-like syntax.
- **Parsing:** The internal compiler checks for syntax errors and breaks the code down into a structured "Parse Tree."
- **Bytecode Compilation:** The source code is translated into an intermediate, platform-independent format called **Bytecode** (often saved as `.pyc` files).
- **PVM Loading:** The **Python Virtual Machine (PVM)** loads compiled bytecode into memory.
- **Interpretation & Execution:** The PVM translates that bytecode into machine-specific instructions line-by-line and executes them on your CPU.

### Difference between Compiler and Interpreter

| **Feature**           | **Compiler**                                                                       | **Interpreter**                                                            |
| --------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Translation Unit**  | Translates the **entire** source code at once.                                     | Translates code **line-by-line** as it runs.                               |
| **Output File**       | Generates an intermediate object/executable file (e.g., `.exe`, `.out`).           | No intermediate object code is produced.                                   |
| **Execution Speed**   | **Fast** (since translation is done beforehand).                                   | **Slow** (translation happens during execution).                           |
| **Error Detection**   | Lists **all errors** after scanning the whole file; won't run until all are fixed. | Stops execution at the **first error** it hits; makes debugging immediate. |
| **Memory Usage**      | **Higher** (needs to store the generated machine code).                            | **Lower** (only deals with the current line being executed).               |
| **Development Cycle** | Slower (requires a "build" or "compile" step every time).                          | Faster (you can run changes instantly).                                    |
| **Efficiency**        | Highly optimized for the specific hardware it was built for.                       | Less optimized; relies on the environment it's running in.                 |
| **Examples**          | C, C++, Rust, Swift, Go.                                                           | Python, JavaScript, Ruby, PHP.                                             |
### Difference Between Python and C++

|Criteria|Python|C++|
|---|---|---|
|Execution|Python is an interpreted-based programming language. Python programs are interpreted by an interpreter.|C++ is a compiler-based programming language. C++ programs are compiled by a compiler.|
|Typing|Python is a dynamic-typed language.|C++ is a static-typed language.|
|Portability|Python is a highly portable language, code written and executed on a system can be easily run on another system.|C++ is not a portable language, code written and executed on a system cannot be run on another system without making changes.|
|Garbage collection|Python provides a garbage collection feature. You do not need to worry about the memory management. It is automatic in Python.|C++ does not provide garbage collection. You have to take care of freeing memories. It is manual in C++.|
|Syntax|Python's syntaxes are very easy to read, write, and understand.|C++'s syntaxes are tedious.|
|Performance|Python's execution performance is slower than C++'s.|C++ codes are faster than Python codes.|
|Application areas|Python's application areas are machine learning, web applications, and more.|C++'s application areas are embedded systems, device drivers, and more.|
## Variables
Based on the tutorial content provided, here is a one-line explanation for each key concept:

- **Python Variables:** Symbolic names that serve as references or pointers to objects stored in memory.
- **Memory Addresses:** The specific numerical locations in a computer's RAM where data objects are stored, accessible via the `id()` function.

```
# Variable serves as a reference 
x = [1, 2, 3] 
y = x          # Both x and y now point to the same list object

# Check memory addresses
print(id(x))
print(id(y))   # These will be identical
```

- **Creating Variables:** Variables are created automatically the moment you assign a value to them using the `=` operator.
- **Printing Variables:** The `print()` function is used to display the value currently held by a variable.

```
# Creation via assignment
message = "Hello, Python!"

# Displaying the value
print(message)
```

- **Deleting Variables:** The `del` statement removes the reference to an object, making the variable name undefined.
```
score = 100
del score

# This would raise a NameError because 'score' no longer exists
# print(score)
```

- **Getting Type:** The `type()` function identifies the data category (like `int`, `str`, or `float`) of a variable.
- **Casting:** The process of explicitly converting a variable from one data type to another using constructor functions like `int()` or `str()`.

```
# Getting type
val = 10.5
print(type(val)) # <class 'float'>

# Casting
age = "25"       # Currently a string
age_int = int(age) # Converted to integer
print(type(age_int))
```

- **Case-Sensitivity:** Python treats uppercase and lowercase identifiers as entirely distinct variables (e.g., `age` vs `Age`).

```
age = 20
Age = 30

print(age) # Outputs 20
print(Age) # Outputs 30
```

- **Multiple Assignment:** Python allows you to assign one value to multiple variables or multiple values to multiple variables in a single line.

```
# Assigning different values to different variables
a, b, c = 1, 2, "Three"

# Assigning the same value to multiple variables
x = y = z = 0
```

- **Naming Conventions:** Rules requiring variables to start with letters/underscores and use styles like Pascal case, CamelCase or Snake_case for readability.

```
# snake_case (Standard for variables)
user_first_name = "Guido"

# camelCase (Common in other languages, less so in Python)
userFirstName = "Guido"

# Variables cannot start with a number (e.g., 1variable is invalid)

# Pascal case: First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre
```

- **Local Variables:** Variables defined inside a function that can only be accessed within that specific function's scope.
- **Global Variables:** Variables defined outside of functions that can be accessed and used throughout the entire program.

```
global_var = "I am everywhere"

def my_function():
    local_var = "I am only inside here"
    print(local_var)
    print(global_var)

my_function()
# print(local_var) # This would fail!
```

- **Constants:** Variables intended to remain unchanged, conventionally named in all-caps (screaming snake case) to signal their purpose.
```
PI = 3.14159
MAX_CONNECTIONS = 100
```

- **Python vs C/C++ Variables:** Unlike C/C++, where variables are fixed memory "containers," Python variables are "labels" that point to objects in memory.

## Data Types

Data types in Python are classes that categorise values to determine what operations can be performed on them and how they are represented in memory.

|**Category**|**Data Type(s)**|**Description**|
|---|---|---|
|**Text**|`str`|Represents sequences of Unicode characters.|
|**Numeric**|`int`, `float`, `complex`|Handles integers, floating-point decimals, and complex numbers.|
|**Sequence**|`list`, `tuple`, `range`|Represents ordered collections (mutable, immutable, or generated).|
|**Mapping**|`dict`|Stores data in key-value pairs for fast lookups.|
|**Set**|`set`, `frozenset`|Collections of unique items (mutable or immutable).|
|**Boolean**|`bool`|Represents logical values: **True** or **False**.|
|**Binary**|`bytes`, `bytearray`, `memoryview`|Used for manipulating raw binary data and buffers.|
|**None**|`NoneType`|A special type representing the absence of a value.|

### Data Type: Code Examples:
```
# Text Type
x_str = "Hello World"

# Numeric Types
x_int = 20
x_float = 20.5
x_complex = 1j

# Sequence Types
x_list = ["apple", "banana", "cherry"]
x_tuple = ("apple", "banana", "cherry")
x_range = range(6)

# Mapping Type
x_dict = {"name": "Alice", "age": 25}

# Set Types
x_set = {"apple", "banana", "cherry"}
x_frozenset = frozenset({"apple", "banana", "cherry"})

# Boolean Type
x_bool = True

# Binary Types
x_bytes = b"Hello"
x_bytearray = bytearray(5)
x_memoryview = memoryview(bytes(5))

# None Type
x_none = None

# To check a type, you can use the type() function:
print(type(x_list))  # Output: <class 'list'>
```

## Type Casting

**Definition:** The process of converting an object from one data type to another to enable specific operations.

```
x = float(5)
print(x) 

# Output: 5.0
```

### A. Implicit Casting

**Definition:** Python automatically converts a "smaller" data type (like `int`) to a "larger" one (like `float`) during arithmetic to prevent data loss.

```
result = 10 + 10.5
print(result, type(result)) 

# Output: 20.5 <class 'float'>
```

### B. Explicit Casting

**Definition:** The manual conversion of data types by a programmer using built-in constructor functions.

```
val = int("100")
print(val, type(val)) 

# Output: 100 <class 'int'>
```

### C. Integer Conversion (`int()`)

**Definition:** Converts a float (by truncating decimals) or a valid numeric string into an integer.

```
print(int(10.9), int("20")) 

# Output: 10 20
```

### D. Base Conversion with `int()`

**Definition:** Converts strings of different number systems (Binary, Octal, Hex) into decimal integers by specifying the base.

```
print(int("110", 2), int("2A", 16)) 

# Output: 6 42
```

### E. Floating-Point Conversion (`float()`)

**Definition:** Converts integers or numeric strings into decimal numbers, supporting scientific notation as well.

```
print(float(5), float("1.2E-2")) 

# Output: 5.0 0.012
```

### F. String Conversion (`str()`)

**Definition:** Returns the string representation of any object, including numbers, lists, and booleans.
```
print(str(True), str([1, 2])) 

# Output: 'True' '[1, 2]'
```

### G. Sequence Conversion (`list()` / `tuple()`)

**Definition:** Converts iterable objects like strings or other sequences into a list (mutable) or a tuple (immutable).

```
print(list("ABC"), tuple([1, 2])) 

# Output: ['A', 'B', 'C'] (1, 2)
```

### H. Data Conversion Functions

| **Function Name**         | **Description**                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------ |
| **`int(x, base=10)`**     | Converts $x$ to an integer. The `base` parameter is used if $x$ is a string (e.g., base 2 for binary). |
| **`float(x)`**            | Converts $x$ to a floating-point number.                                                               |
| **`complex(real, imag)`** | Creates a complex number with the value $real + imag \cdot j$.                                         |
| **`str(x)`**              | Converts object $x$ to a readable string representation.                                               |
| **`repr(x)`**             | Converts object $x$ to an expression string (useful for debugging).                                    |
| **`eval(str)`**           | Evaluates a string as a Python expression and returns the resulting object.                            |
| **`tuple(s)`**            | Converts an iterable $s$ (like a list or string) into a tuple.                                         |
| **`list(s)`**             | Converts an iterable $s$ into a list.                                                                  |
| **`set(s)`**              | Converts an iterable $s$ into a set (removing duplicates).                                             |
| **`dict(d)`**             | Creates a dictionary. $d$ must be a sequence of `(key, value)` tuples.                                 |
| **`frozenset(s)`**        | Converts an iterable $s$ into an immutable set.                                                        |
| **`chr(x)`**              | Converts an integer (Unicode code point) to its character string.                                      |
| **`ord(c)`**              | Converts a single character $c$ to its integer Unicode code point value.                               |
| **`hex(x)`**              | Converts an integer $x$ to a lowercase hexadecimal string prefixed with `0x`.                          |
| **`oct(x)`**              | Converts an integer $x$ to an octal string prefixed with `0o`.                                         |
| **`bin(x)`**              | Converts an integer $x$ to a binary string prefixed with `0b`.                                         |
### I. Dunder Methods (Double Underscore)

- Dunder methods act as internal "hooks" that the Python interpreter automatically triggers when specific built-in syntax, operators, or functions (like `+`, `len()`, or `for` loops) are applied to an object.
- Custom objects are converted to built-in types by defining **Dunder (Double Underscore) Methods**. When you call a function like `int(obj)`, Python looks for a method named `__int__` inside that object's class.

|**Built-in Function**|**Dunder Method**|**Purpose**|
|---|---|---|
|`str(obj)`|`__str__(self)`|Returns a user-friendly string representation.|
|`repr(obj)`|`__repr__(self)`|Returns a developer-friendly "official" string.|
|`int(obj)`|`__int__(self)`|Defines how to convert the object to an integer.|
|`float(obj)`|`__float__(self)`|Defines how to convert the object to a float.|
|`bool(obj)`|`__bool__(self)`|Defines if the object is considered `True` or `False`.|
#### Code Example: A "Price" Object

Imagine you have a class that stores a price with a currency. You want to be able to turn it into an integer for math or a string for a receipt
```
class ProductPrice:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    # Controls what str() returns
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    # Controls what int() returns
    def __int__(self):
        return int(self.amount)

    # Controls what float() returns
    def __float__(self):
        return float(self.amount)

# Creating the object
price = ProductPrice(24.99)

# Testing the conversions
print(f"As a string: {str(price)}")    # Output: USD 24.99
print(f"As an integer: {int(price)}")  # Output: 24 (decimals dropped)
print(f"As a float: {float(price)}")   # Output: 24.99
```

## Unicode System

Python 3 treats all strings as **Unicode** by default, allowing your programs to handle text from virtually any language or symbol set seamlessly.

### A. The Unicode Standard

**Definition:** A universal character set where every character—regardless of language or platform—is assigned a unique numeric value called a "Code Point."

```
# Using a Unicode escape sequence for the fraction 3/4

var = "\u00BE"

print(var)

# Output: ¾
```

### B. Character Encoding (UTF-8)

**Definition:** The set of rules (like UTF-8, UTF-16, or UTF-32) used to translate numeric code points into a sequence of 8-bit bytes for memory storage.

```
# Python's source code and strings default to UTF-8
text = "Hello"

print(text)

# Output: Hello
```

### C. String Encoding (`str` to `bytes`)

**Definition:** The process of converting a human-readable string into a series of bytes (binary data) using the `.encode()` method.

Python

```
string = "₹"

tobytes = string.encode('utf-8')

print(tobytes)

# Output: b'\xe2\x82\xb9'
```

### D. String Decoding (`bytes` to `str`)

**Definition:** The process of translating raw binary data back into a human-readable character string using the `.decode()` method.

Python

```
raw_data = b'\xe2\x82\xb9'

original_string = raw_data.decode('utf-8')

print(original_string)

# Output: ₹
```

### E. Unicode Escape Sequences

**Definition:** A way to represent characters in code using their hex code point values (prefixed by `\u` or `\U`) instead of typing the literal symbol.

Python

```
# Representing "10" using Unicode values for '1' and '0'

var = "\u0031\u0030"

print(var)

# Output: 10
```

### F. Summary Table for Revision
| **Concept**  | **Direction**               | **Method**       | **Result Type** |
| ------------ | --------------------------- | ---------------- | --------------- |
| **Encoding** | Human $\rightarrow$ Machine | `str.encode()`   | `bytes`         |
| **Decoding** | Machine $\rightarrow$ Human | `bytes.decode()` | `str`           |

### G. Understanding UTF (Unicode Transformation Format)

In simple terms, if **Unicode** is a giant dictionary where every character has a unique ID number (a code point), **UTF** is the set of instructions on how to actually write those numbers down in binary so a computer can read them.

#### 1. The Three Types of UTF

| **Type**   | **Definition**                                                                                             | **Memory Usage**                                                        | **Best For...**                                         |
| ---------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| **UTF-8**  | A variable-width encoding that uses 1 to 4 bytes per character and is 100% backward compatible with ASCII. | **Efficient:** 1 byte for English, more for others.                     | The Web, most files, and general-purpose Python coding. |
| **UTF-16** | A variable-width encoding that uses either 2 or 4 bytes for every character.                               | **Moderate:** Good for Asian languages where characters fit in 2 bytes. | Windows internal strings and Java environments.         |
| **UTF-32** | A fixed-width encoding that uses exactly 4 bytes (32 bits) for every single character.                     | **Heavy:** Uses the most memory but is fast for indexing.               | Internal processing where memory isn't an issue.        |

#### 2. UTF-8 (The Industry Standard)

**Definition:** The most popular encoding because it saves space by using only 1 byte for standard English characters while expanding as needed for emojis or special symbols.

```
text = "A" # Standard ASCII

print(f"UTF-8 'A': {text.encode('utf-8')}") 

# Output: b'A' (Only 1 byte)

emoji = "🐍"

print(f"UTF-8 Snake: {emoji.encode('utf-8')}")


# Output: b'\xf0\x9f\x90\x8d' (4 bytes)
```

#### 3. UTF-16 (The Middle Ground)

**Definition:** It treats most common characters as 2-byte units, which can be more efficient for non-Latin scripts but doubles the size of English text compared to UTF-8.

```
text = "A"

print(f"UTF-16 'A': {text.encode('utf-16')}")

# Output: b'\xff\xfeA\x00' (The \xff\xfe is a 'Byte Order Mark')
```

#### 4. UTF-32 (The Fixed-Width Option)

**Definition:** Every character gets 4 bytes, making it predictable for the computer to find the "10th character" in a string, though it's quite a memory hog.

```
text = "A"

print(f"UTF-32 'A': {text.encode('utf-32')}")

# Output: b'\xff\xfe\x00\x00A\x00\x00\x00' (Exactly 4 bytes for data)
```

## Operators

**Python operators** are special symbols or keywords used to perform specific operations on variables and values (operands).

### A. Arithmetic Operators

Arithmetic operators are used to perform basic mathematical calculations like addition and subtraction.

| **Operator** | **Name**            | **Example (a=10, b=20)** |
| ------------ | ------------------- | ------------------------ |
| `+`          | Addition            | `a + b = 30`             |
| `-`          | Subtraction         | `a - b = -10`            |
| `*`          | Multiplication      | `a * b = 200`            |
| `/`          | Division            | `b / a = 2.0`            |
| `%`          | Modulus (Remainder) | `b % a = 0`              |
| `**`         | Exponent (Power)    | `a ** b`                 |
| `//`         | Floor Division      | `9 // 2 = 4`             |

### B. Comparison (Relational) Operators

Comparison operators evaluate the relationship between two operands and return a Boolean value (`True` or `False`).

|**Operator**|**Name**|**Example (a=10, b=20)**|
|---|---|---|
|`==`|Equal|`a == b` is False|
|`!=`|Not equal|`a != b` is True|
|`>`|Greater than|`a > b` is False|
|`<`|Less than|`a < b` is True|
|`>=`|Greater than or equal to|`a >= b` is False|
|`<=`|Less than or equal to|`a <= b` is True|

### C. Assignment Operators

Assignment operators are used to assign new values to variables, often combining an operation with the assignment.

|**Operator**|**Example**|**Equivalent To**|
|---|---|---|
|`=`|`a = 10`|`a = 10`|
|`+=`|`a += 5`|`a = a + 5`|
|`-=`|`a -= 5`|`a = a - 5`|
|`*=`|`a *= 5`|`a = a * 5`|
|`/=`|`a /= 5`|`a = a / 5`|
|`%=`|`a %= 5`|`a = a % 5`|
|`**=`|`a **= 5`|`a = a ** 5`|
|`//=`|`a //= 5`|`a = a // 5`|

### D. Bitwise Operators

Bitwise operators perform operations directly on the binary representations (bits) of numbers.

|**Operator**|**Name**|**Description**|
|---|---|---|
|`&`|AND|Sets each bit to 1 if both bits are 1|
|`\|`|OR|Sets each bit to 1 if one of two bits is 1|
|`^`|XOR|Sets each bit to 1 if only one of two bits is 1|
|`~`|NOT|Inverts all the bits|
|`<<`|Zero fill left shift|Shifts bits left by pushing zeros in from the right|
|`>>`|Signed right shift|Shifts bits right by pushing copies of the leftmost bit|

### E. Logical Operators

Logical operators are used to combine multiple conditional statements.

| **Operator** | **Name**    | **Description**                               |
| ------------ | ----------- | --------------------------------------------- |
| `and`        | Logical AND | Returns True if both statements are true      |
| `or`         | Logical OR  | Returns True if one of the statements is true |
| `not`        | Logical NOT | Reverses the result (True becomes False)      |

### F. Membership Operators

Membership operators test if a specific value or variable is found within a sequence (string, list, or tuple).

|**Operator**|**Description**|**Example**|
|---|---|---|
|`in`|Returns True if value is present in the sequence|`x in y`|
|`not in`|Returns True if value is NOT present in the sequence|`x not in y`|

### G. Identity Operators

Identity operators compare the memory location of two objects to see if they are actually the same instance.

|**Operator**|**Description**|**Example**|
|---|---|---|
|`is`|Returns True if both variables point to the same object|`x is y`|
|`is not`|Returns True if both variables point to different objects|`x is not y`|

### H. Operator Precedence (Highest to Lowest)

Precedence determines the order in which operations are evaluated in an expression.

|**Level**|**Operators**|**Description**|
|---|---|---|
|1|`**`|Exponentiation|
|2|`~`, `+`, `-`|Complement, Unary plus/minus|
|3|`*`, `/`, `%`, `//`|Multiplication, Division, Modulo, Floor division|
|4|`+`, `-`|Addition and Subtraction|
|5|`>>`, `<<`|Bitwise shifts|
|6|`&`|Bitwise AND|
|7|`^`, `\|`|Bitwise XOR and OR|
|8|`<=`, `<`, `>`, `>=`|Comparison operators|
|9|`==`, `!=`|Equality operators|
|10|`=`, `%=`, `+=`, etc.|Assignment operators|
|11|`is`, `is not`|Identity operators|
|12|`in`, `not in`|Membership operators|
|13|`not`, `or`, `and`|Logical operators|
### I. Membership Operators

Membership operators are used to test whether a value or variable is found within a sequence (such as strings, lists, tuples, sets, or dictionaries).

**Quick Tip:** Membership testing is case-sensitive for strings and generally highly efficient for sets and dictionaries compared to lists.

#### 1. The `in` Operator

**Definition:** Returns `True` if the specified value exists within the given container, and `False` otherwise.

```
var = "TutorialsPoint"
print("P in var:", "P" in var)
# Output: P in var: True
```

#### 2. The `not in` Operator

**Definition:** Returns `True` if the specified value is absent from the container, and `False` if the value is found.

```
var = [10, 20, 30, 40]
print("50 not in var:", 50 not in var)
# Output: 50 not in var: True
```

#### 3. Usage with Sequences (Lists & Tuples)

**Definition:** Checks if an individual element exists as a top-level member of the list or tuple.

```
# Note: Nested sequences must match exactly to return True
var = (10, 20, 30, 40)
print("(10, 20) in var:", (10, 20) in var)
# Output: (10, 20) in var: False
```

#### 4. Usage with Sets

**Definition:** Evaluates whether an item is part of the unordered collection of unique elements.

```
var = {10, 20, 30, 40}
print("20 in var:", 20 in var)
# Output: 20 in var: True
```

#### 5. Usage with Dictionaries

**Definition:** Checks for the presence of a specific **key** within the dictionary, ignoring the values.

```
var = {1: 10, 2: 20}

print("2 in var:", 2 in var)

print("20 in var:", 20 in var)

# Output: 
# 2 in var: True
# 20 in var: False
```

### J. Identity Operators

Identity operators are used to determine if two variables point to the **exact same object** in memory, rather than just having the same value.

#### 1. The `is` Operator

**Definition:** Returns `True` if both variables point to the same memory location (shared ID), and `False` otherwise.

```
a = [1, 2, 3]
b = a  # b points to the same object as a
c = [1, 2, 3] # c is a new object with the same values

print("a is b:", a is b)
print("a is c:", a is c)
# Output: 
# a is b: True
# a is c: False
```

#### 2. The `is not` Operator

**Definition:** Returns `True` if the variables point to different objects in memory, even if their contents are identical.

```
a = [1, 2, 3]
b = [1, 2, 3]
print("a is not b:", a is not b)
# Output: a is not b: True
```

#### 3. The `id()` Function

**Definition:** Returns the unique integer identity (memory address) of an object, which is used by identity operators for comparison.

```
x = "Python"
y = x
print(id(x) == id(y))
# Output: True
```


#### 4. Key Takeaway: Identity (`is`) vs. Equality (`==`)

- **`==` (Equality):** Checks if the **values** are the same (e.g., two different wallets both containing $10).
- **`is` (Identity):** Checks if they are the **exact same instance** (e.g., two people talking about the same physical wallet).

## Comments

Comments are programmer-readable annotations in the source code that are ignored by the Python interpreter and used to make code easier to understand.

### A. Single-Line Comments

**Definition:** Starts with a hash symbol (`#`) and continues to the end of the line, used for short notes.

```
# This is a standalone comment
print("Hello!")  # This is an inline comment
# Output: Hello!
```

### B. Multi-Line Comments (Consecutive)

**Definition:** Created by placing a hash symbol (`#`) at the start of each individual line to explain complex logic.

```
# This function adds two numbers
# and returns the total sum
def add(a, b):
    return a + b
```

### C. Multi-Line Comments (Triple Quotes)

**Definition:** Uses `'''` or `"""` to wrap text; technically string literals, they act as comments when not assigned to a variable.

```
"""
This is a multi-line string
used as a block comment
to explain this section.
"""
print("Logic executed")
# Output: Logic executed
```

### D. Docstrings (Documentation Strings)

**Definition:** Special triple-quoted comments placed immediately after a function, class, or module definition to describe its purpose.

```
def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

print(multiply.__doc__)
# Output: Multiplies two numbers and returns the result.
```

### E. Accessing Documentation

**Definition:** Docstrings can be retrieved programmatically using the `.__doc__` attribute or the built-in `help()` function.

```
def example():
    """Example docstring."""
    pass

help(example)
# Output: Help on function example in module __main__: example() Example docstring.
```


> **Note:** While `#` is for internal developer notes, **Docstrings** are meant for anyone using your code to understand how to interact with your functions or classes.

## Input & Output

### A. The `input()` Function

**Definition:** Captures user input as a **string** and optionally displays a prompt message.

```
name = input("Enter your name: ")

print(f"Hello, {name}!") 

# Output: Hello, [User Input]!
```

### B. Type Casting with Type Hinting

**Definition:** Converts the default string input into other types (like `int` or `float`) to allow calculations, often clarified by "Type Hinting" variables.

```
# 'age: int' is a type hint (it informs the developer the variable should be an integer)

age: int = int(input("Enter your age: "))

print(f"Next year, you will be {age + 1}.")

# Output (if 25 is entered): Next year, you will be 26.
```

### C. Modern Formatting: F-Strings

**Definition:** Introduced in Python 3.6, **Formatted String Literals** (f-strings) allow you to embed expressions inside string literals using curly braces `{}`.

```
price: float = 49.99

quantity: int = 3

# F-strings are faster and more readable than comma-separation

print(f"Total Cost: ${price * quantity}")

# Output: Total Cost: $149.97
```

### D. Advanced `print()` Control

**Definition:** The `print()` function uses `sep` to define what goes between items and `end` to define what happens at the conclusion of the line.

```
# Using 'sep' for custom separators and 'end' to prevent a newline

print("Python", "is", "powerful", sep="-", end="!!")

# Output: Python-is-powerful!!
```

### E. Practical Example: Area Calculator

This script demonstrates **Type Hinting**, **Input Casting**, and **F-strings** all in one:

```
# Providing clear type hints for the variables

width: float = float(input("Enter width: "))
height: float = float(input("Enter height: "))

area: float = width * height

# Using f-string for a clean, readable result

print(f"The area of a {width}x{height} rectangle is {area}.")
```

## Control Flow

Control flow statements determine the order in which code is executed, allowing for decision-making, repetition, and structural jumps.

### A. Sequential Execution

**Definition:** The default behavior where Python executes instructions one after another, from top to bottom.

```
x = 5
y = 10
print(f"Sum: {x + y}")
# Output: Sum: 15
```

### B. Decision Making: `if-elif-else`

**Definition:** Executes specific blocks of code based on whether a Boolean condition evaluates to `True`.

```
marks: int = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")
# Output: Grade: B
```

### C. Iteration: `for` Loop

**Definition:** Iterates over a sequence (list, tuple, string) or a range of numbers.

```
for i in range(3):
    print(f"Iteration {i}")
# Output: 
# Iteration 0
# Iteration 1
# Iteration 2
```

### D. Iteration: `while` Loop

**Definition:** Repeats a block of code as long as a specified condition remains `True`.

```
count: int = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1
# Output:
# Count: 1
# Count: 2
# Count: 3
```

### E. Loop Control: `break`, `continue`, and `pass`

**Definition:** `break` exits the loop entirely; `continue` skips to the next iteration; `pass` is a null placeholder used to avoid syntax errors in empty code blocks.

```
for n in range(1, 6):
    if n == 2:
        continue  # Skip the rest of this iteration
    if n == 4:
        break     # Exit the loop entirely
    if n == 3:
        pass      # Placeholder: does nothing, just moves to next line
    print(f"Number: {n}")
# Output:
# Number: 1
# Number: 3
```


### F. Loop with `else` Clause

**Definition:** A unique Python feature where the `else` block executes only if the loop finished naturally (without hitting a `break`).

```
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
# Output:
# 0
# 1
# 2
# Loop finished successfully!
```

### G. Nested Control Flow

**Definition:** Placing a conditional statement or loop inside another to handle complex multi-layered logic.

```
groups: list = [[1, 2], [3, 4]]
for group in groups:
    for item in group:
        if item % 2 == 0:
            print(f"Even: {item}")
# Output:
# Even: 2
# Even: 4
```

### H. Modern Best Practice

In modern Python, while **nested loops** are powerful, developers often use **List Comprehensions** or the `itertools` module to keep code "flat" and more readable.

## Functions

**Definition:** A block of organised, reusable code used to perform a single, related action. Functions provide better modularity for an application and enable a high degree of code reuse.

### A. Types of Python Functions

|**Type**|**Description**|
|---|---|
|**Built-in Functions**|Functions included in Python's standard library that are always available in memory (e.g., `print()`, `int()`, `len()`).|
|**Module Functions**|Functions defined inside built-in or external modules. They must be imported into memory before use.|
|**User-defined Functions**|Custom functions created by the developer to perform specific, tailored operations.|

### B. Defining and Calling a Function

**Definition:** Functions are defined using the `def` keyword, followed by the function name, parentheses (which may contain parameters), and a colon. The code block must be indented.

```
# Defining the function
def greetings(name):
    """This is a docstring explaining the function."""
    print(f"Hello {name}")
    return

# Calling the function
greetings("Samay")

# Output: Hello Samay
```

### C. Pass by Reference vs. Value

In Python, variables act as labels pointing to objects in memory. Python uses a **"pass by object reference"** mechanism.

- **Immutable Objects (e.g., Integers, Strings):** If you pass an integer and modify it inside the function, Python creates a _new_ object. The original variable outside the function remains unchanged.
- **Mutable Objects (e.g., Lists, Dictionaries):** If you pass a list and modify it (like appending an item), the original list outside the function is also updated because both point to the exact same memory address.

```
# Mutable Object Example
def add_item(my_list):
    my_list.append(100)

numbers = [10, 20, 30]
add_item(numbers)

print(numbers)
# Output: [10, 20, 30, 100]
```
### D. Types of Function Arguments

#### 1. Positional (Required) Arguments

**Definition:** Arguments passed in the exact positional order defined by the function. The number of arguments must match exactly.

```
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info("Alice", 30)

# Output: Name: Alice, Age: 30
```
#### 2. Keyword Arguments

**Definition:** Arguments passed using the parameter name. This allows you to place them out of order since Python matches them by keyword.

```
print_info(age=50, name="Miki")
# Output: Name: Miki, Age: 50
```
#### 3. Default Arguments

**Definition:** Arguments that assume a default value if no value is provided in the function call.

```
def print_user(name, role="Guest"):
    print(f"{name} is a {role}")

print_user("Alice")
# Output: Alice is a Guest
```
#### 4. Positional-Only Arguments (`/`)

**Definition:** Arguments that _must_ be specified by position and cannot be passed as keywords. Placed before a `/` symbol.

```
def pos_fun(x, y, /, z):
    print(x + y + z)

pos_fun(33, 22, z=11)
# Output: 66
```
#### 5. Keyword-Only Arguments (`*`)

**Definition:** Arguments that _must_ be specified by their keyword. Placed after an `*` symbol.

```
def kw_fun(*, num1, num2):
    print(num1 * num2)

kw_fun(num1=6, num2=8)
# Output: 48
```
#### 6. Arbitrary (Variable-Length) Arguments (`*args`)

**Definition:** Allows a function to accept any number of positional arguments, packing them into a tuple.

```
def print_all(*args):
    for arg in args:
        print(arg, end=" ")

print_all(10, 20, 30)
# Output: 10 20 30
```
### E. Order of Python Function Arguments

When combining different types of arguments in a single function, they **must** be declared in this specific order:

1. **Positional-only arguments** (followed by `/`)
2. **Regular positional arguments**
3. **Default arguments**
4. **Arbitrary positional arguments** (`*args`)
5. **Keyword-only arguments**
6. **Arbitrary keyword arguments** (`kwargs`)
### F. Return Values

**Definition:** The `return` keyword ends the function execution and sends the result of an expression back to the caller. If no expression is provided, it returns `None`.

```
def add(x, y):
    return x + y

result = add(10, 20)
print(f"Total: {result}")
# Output: Total: 30
```
### G. Anonymous Functions (`lambda`)

**Definition:** Small, single-line functions created without the `def` keyword. They can take multiple arguments but only execute a single expression.

**Syntax:** `lambda [arguments]: expression`

```
# Defining a lambda function
sum_nums = lambda arg1, arg2: arg1 + arg2

print(f"Value: {sum_nums(10, 20)}")
# Output: Value: 30
```

### H. Variable Scope

The scope of a variable determines where in the program it can be accessed.

- **Local Scope:** Variables created inside a function. They can only be used within that specific function.
- **Global Scope:** Variables created outside of any function. They can be accessed from anywhere in the file.

```
total = 0  # Global variable

def calculate_sum(a, b):
    total = a + b  # Local variable (shadows the global one inside this block)
    print(f"Inside function: {total}")

calculate_sum(10, 20)
print(f"Outside function: {total}")

# Output:
# Inside function: 30
# Outside function: 0
```
### I. Default Arguments

**Definition:** Function arguments that are assigned a predefined value during the function's definition. If the caller does not provide a value for that argument, Python automatically uses the default. If a value is provided, it safely overrides the default.

#### A. Basic Usage

You can selectively override default arguments or rely on the predefined values when calling the function.

```
# Function definition with a default argument for 'city'
def show_info(name, city="Hyderabad"):
   print(f"Name: {name}")
   print(f"City: {city}")
   return

# Calling with both arguments (Overrides the default)
show_info(name="Ansh", city="Delhi")
# Output: 
# Name: Ansh
# City: Delhi

# Calling with only the required argument (Uses the default)
show_info(name="Shrey")
# Output: 
# Name: Shrey
# City: Hyderabad
```

#### B. Combining with Positional Arguments

Default arguments are frequently combined with standard positional arguments.

_(Note: In the function definition, default arguments must always be placed **after** non-default arguments._

```
# 'phy' and 'maths' are required, 'maxmarks' is optional
def calculate_percent(phy, maths, maxmarks=200):
   val = (phy + maths) * 100 / maxmarks
   return val

# Uses the default maxmarks of 200
result_default = calculate_percent(60, 70)
print(f"Percentage: {result_default}")
# Output: Percentage: 65.0

# Overrides the default maxmarks with 100
result_custom = calculate_percent(40, 46, 100)
print(f"Percentage: {result_custom}")
# Output: Percentage: 86.0
```
#### C. The "Mutable Default Argument" Trap

**Important Concept:** Python evaluates default arguments _only once_ when the function is defined, not each time the function is called.

If you use a **mutable object** (like a `list`, `dictionary`, or `set`) as a default argument and modify it inside the function, the same object in memory is updated. Those changes will persist and leak into subsequent function calls.

```
# Using a mutable list as a default argument
def add_to_list(nums, numeric_list=[]):
   numeric_list.append(nums + 1)
   print(numeric_list) 
    
# Function calls
add_to_list(66)
# Output: [67]

add_to_list(68)
# Output: [67, 69]  <-- The list remembered the previous call!

add_to_list(70)
# Output: [67, 69, 71]
```
### J. Keyword Arguments

**Definition:** Function arguments are passed by explicitly naming the parameter (e.g., `parameter_name=value`) during the function call. This allows you to pass arguments out of their defined order, as Python matches them by their keyword rather than their position.
#### A. Basic Usage

You can call a function using standard positional arguments, or you can explicitly state the keywords to make the function call more readable.

```
# Function definition
def print_info(name, age):
   print(f"Name: {name}")
   print(f"Age: {age}")
   return

# Calling via positional arguments (order matters)
print_info("Naveen", 29)
# Output: 
# Name: Naveen
# Age: 29

# Calling via keyword arguments (explicit naming)
print_info(name="Miki", age=30)
# Output: 
# Name: Miki
# Age: 30
```
#### B. Independence of Order

When you use keyword arguments for all parameters, the order in which you pass them no longer matters. Python routes the values to the correct variables based on the names provided.

```
def division(num, den):
   quotient = num / den
   print(f"num:{num} den:{den} quotient:{quotient}")

# The order is swapped, but the result is exactly the same
division(num=10, den=5)
# Output: num:10 den:5 quotient:2.0

division(den=5, num=10)
# Output: num:10 den:5 quotient:2.0
```

#### C. Mixed Calling & The Positional Rule

You can mix positional and keyword arguments in a single function call. However, **positional arguments must always appear before keyword arguments**.

If a positional argument is placed after a keyword argument, Python will throw an error because it can no longer safely guess which position the remaining arguments belong to.

```
def division(num, den):
   return num / den

# Correct: Positional first, Keyword second
result = division(10, den=5) 
print(result) # Output: 2.0

# Incorrect: Keyword first, Positional second
# result = division(num=10, 5)

# This will raise a SyntaxError:
# SyntaxError: positional argument follows keyword argument
```

### K. Positional Arguments

**Definition:** The most fundamental type of argument in Python. The values passed into the function call are assigned to the parameters in the exact structural order they were defined.

#### A. Key Rules for Positional Arguments

When utilising positional arguments, you must adhere to several strict guidelines:

- **Completeness:** All defined positional arguments are strictly required to execute the function.
- **Count Matching:** The total number of actual arguments passed must equal the exact number of formal arguments defined in the function signature.
- **Sequential Assignment:** Values are picked up and mapped to variables purely based on their order.
- **Type Compatibility:** The data types passed must support the operations performed within the function block.
- **Name Independence:** The variable names passed into the function do not need to match the parameter names defined in the function.
#### B. Basic Usage (Correct Mapping)

Positional arguments are mapped sequentially. In the example below, the first value seamlessly maps to `x` and the second maps to `y`.

```
def add(x, y):
   z = x + y
   print(f"x={x} y={y} x+y={z}")

a = 10
b = 20

# 'a' maps to 'x', 'b' maps to 'y' based entirely on position
add(a, b)
# Output: x=10 y=20 x+y=30
```

#### C. Common Errors with Positional Arguments

**1. Missing Arguments:** Python will immediately raise an error if you fail to provide enough arguments to satisfy the function's definition.

```
def add(x, y):
   return x + y

a = 10
# add(a) 

# This will raise a TypeError:
# TypeError: add() missing 1 required positional argument: 'y'
```

**2. Too Many Arguments:** Similarly, providing more arguments than the function has parameters for will result in an immediate error.

```
def add(x, y):
   return x + y

# add(10, 20, 30)

# This will raise a TypeError:
# TypeError: add() takes 2 positional arguments but 3 were given
```

**3. Type Mismatches:** While Python is dynamically typed, the actual arguments passed must be of a data type that is logically compatible with the operations happening inside the function.

```
def add(x, y):
   return x + y

a = "Hello"
b = 20

# add(a, b)

# This will raise a TypeError because Python cannot mathematically add a string and an integer:
# TypeError: can only concatenate str (not "int") to str
```
#### D. Positional vs. Keyword Arguments

|**Feature**|**Positional Argument**|**Keyword Argument**|
|---|---|---|
|**Assignment Method**|Values are mapped based purely on their structural order.|Values are mapped explicitly using the parameter name (`name=value`).|
|**Flexibility**|Strict. Arguments **must** be passed in the exact order defined in the function signature.|Flexible. The order of arguments can be rearranged freely during the function call.|
|**Syntax Example**|`function(param1, param2)`|`function(param2=value2, param1=value1)`|
### L. Arbitrary Arguments (`*args` and `kwargs`)

**Definition:** Python allows you to define functions that can accept a variable (arbitrary) number of arguments. This is useful when you don't know beforehand exactly how many arguments will be passed to the function.

#### A. Arbitrary Positional Arguments (`*args`)

**Definition:** By prefixing an argument with a single asterisk (`*`), Python packs all remaining positional arguments passed to the function into a **tuple**.

```
# The *args parameter catches all extra positional arguments
def add_all(*args):
   total = 0
   for num in args:  # 'args' acts as a tuple
      total += num
   return total

print(add_all(10, 20, 30, 40)) 
# Output: 100
```

#### B. Arbitrary Keyword Arguments (`kwargs`)

**Definition:** By prefixing an argument with two asterisks (), Python packs all remaining keyword arguments passed to the function into a **dictionary** of key-value pairs.

```
# The **kwargs parameter catches extra keyword arguments
def print_address(**kwargs):
   for key, value in kwargs.items(): # 'kwargs' acts as a dictionary
      print(f"{key}: {value}")

print_address(Name="Raam", City="Mumbai", PIN="400001")
# Output:
# Name: Raam
# City: Mumbai
# PIN: 400001
```

#### C. The Golden Rule of Argument Order

If a function uses a mix of different argument types, you **must** define them in this specific order to avoid syntax errors:

1. Standard / Required Positional Arguments
2. Arbitrary Positional Arguments (`*args`)
3. Standard Keyword Arguments
4. Arbitrary Keyword Arguments (`kwargs`)

## Variable Scope

**Definition:** Scope defines the specific region of a program where a variable is accessible. Python restricts variable access based on where it was created.

|**Scope Type**|**Definition**|**Accessibility**|
|---|---|---|
|**Local**|Variables created inside a specific function or block.|Can only be used inside that specific function.|
|**Global**|Variables created outside of any function, in the main body of the script.|Can be read from anywhere in the file.|
|**Nonlocal**|Variables used in nested functions (a function inside a function) that are not strictly local or global.|Can be modified by the inner nested function.|

### A. Modifying Global Variables (`global`)

If you try to change a global variable's value from inside a function directly, Python will throw an error (it thinks you are trying to create a local variable before assigning it). You must use the `global` keyword to declare your intent to modify the outer variable.

```
marks = 50 # Global variable

def update_marks():
   global marks  # Tells Python to use the global 'marks', not make a new one
   marks = marks + 20

update_marks()
print(marks) 
# Output: 70
```

#### B. Modifying Nonlocal Variables (`nonlocal`)

Used primarily in nested functions to modify a variable defined in the immediate outer function's scope.

```
def outer_function():
   a = 5
   
   def inner_function():
      nonlocal a # Points to 'a' in outer_function
      a = 10
      return a
      
   return inner_function()

print(outer_function())
# Output: 10
```

## Namespaces

**Definition:** A namespace is a behind-the-scenes dictionary Python uses to map variable names (identifiers) to their actual objects in memory, preventing naming conflicts.

#### Types of Namespaces:

1. **Built-in Namespace:** Contains Python's default functions (like `print()`, `len()`). Loaded when Python starts.
2. **Global Namespace:** Contains names defined in the main program level.
3. **Local Namespace:** Contains names defined inside the currently executing function.

#### A. The `globals()` and `locals()` Functions

Python provides built-in functions to view the current dictionaries representing these namespaces.
- **`globals()`:** Returns a dictionary of the current global symbol table.
- **`locals()`:** Returns a dictionary of the variables currently available in the local function's scope.

```
name = "Alice" # Global

def sample_func():
   age = 30 # Local
   print("Locals dictionary:", locals())

sample_func()
# Output: Locals dictionary: {'age': 30}
```

## Function Annotations

**Definition:** Optional metadata you can attach to a function's parameters and return value to explain what data types they expect. Introduced in PEP 3107.

**Important Note:** Python is dynamically typed. Annotations are completely **ignored by Python at runtime**—they do not enforce strict type checking. They are primarily used as documentation for developers, IDEs (like VSCode or PyCharm), and third-party static type checkers (like `mypy`).

### A. Syntax and Usage

You annotate parameters using a colon `:` and the return type using an arrow `->`.

```
# Expects 'a' and 'b' to be integers, and returns an integer
def add_numbers(a: int, b: int) -> int:
   return a + b

# Python won't stop you from passing strings, despite the 'int' annotations!
print(add_numbers("Hello ", "World"))
# Output: Hello World
```

### B. Accessing Annotations

Annotations are stored automatically inside the function object's `__annotations__` dictionary attribute.

```
def division(num: float, den: float) -> float:
   return num / den

print(division.__annotations__)
# Output: {'num': <class 'float'>, 'den': <class 'float'>, 'return': <class 'float'>}
```

### C. Annotations with Default Values

If a parameter has both an annotation and a default value, the default value comes **after** the annotation.

```
# 'b' expects a float, but defaults to 2.0 if nothing is passed
def divide(a: float, b: float = 2.0) -> float:
   return a / b
```




























