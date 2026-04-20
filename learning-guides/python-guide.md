
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



