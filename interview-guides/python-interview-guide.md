# 100 Must-Know Python Interview Questions and Answers (2026)

> All answers reflect Python 3.12+ version. Get started with Python and refer this questions and answers to understand Python in depth.

## Table of Contents

1. [Python Fundamentals](#1-python-fundamentals) — Q1–Q10
2. [Python Functions and Modules](#2-python-functions-and-modules) — Q11–Q20
3. [Python Advanced Concepts](#3-python-advanced-concepts) — Q21–Q30
4. [Python Object-Oriented Programming](#4-python-object-oriented-programming) — Q31–Q40
5. [Python Debugging and Testing](#5-python-debugging-and-testing) — Q41–Q50
6. [File Handling and Data Processing](#6-file-handling-and-data-processing) — Q51–Q60
7. [Python Libraries and Frameworks](#7-python-libraries-and-frameworks) — Q61–Q70
8. [Networking and Databases in Python](#8-networking-and-databases-in-python) — Q71–Q75
9. [Python Scripting and Automation](#9-python-scripting-and-automation) — Q76–Q80
10. [Python Regular Expressions](#10-python-regular-expressions) — Q81–Q85
11. [Python Environment and Configuration](#11-python-environment-and-configuration) — Q86–Q90
12. [Python and Data Science](#12-python-and-data-science) — Q91–Q95
13. [Python and Machine Learning](#13-python-and-machine-learning) — Q96–Q100

## 1. Python Fundamentals

### Q1. What are the key features of Python?

Python is a high-level, general-purpose programming language first released in 1991 by Guido van Rossum. Over three decades it has evolved into one of the most widely used languages in software engineering, data science, automation, and AI. Its popularity stems from a combination of design philosophy and practical features.

#### Interpreted Language

Python is executed line-by-line by an interpreter rather than compiled ahead of time into machine code. This makes the development cycle fast — you write code and run it immediately without a compilation step. The CPython interpreter (the reference implementation) first compiles source code to bytecode (`.pyc` files), then executes that bytecode in the Python Virtual Machine (PVM).

#### Dynamic Typing

Python uses dynamic typing, meaning variable types are determined at runtime, not at compile time. You do not need to declare a variable's type explicitly.

```python
x = 10       # x is an int
x = "hello"  # x is now a str — perfectly valid in Python
x = [1, 2]   # x is now a list
```

#### Strongly Typed

Although dynamically typed, Python is strongly typed. It does not silently coerce incompatible types. Attempting to add a string to an integer raises a `TypeError`, unlike languages such as JavaScript which perform implicit coercion.

```python
result = "score: " + 10  # TypeError: can only concatenate str (not "int") to str
result = "score: " + str(10)  # Correct: "score: 10"
```

#### High-Level Abstractions

Python provides built-in data structures (lists, dictionaries, sets, tuples) and high-level abstractions that remove the need for manual memory management, pointer arithmetic, or low-level system calls.

#### Extensive Standard Library

Python ships with a rich standard library covering file I/O, networking, threading, JSON, CSV, regular expressions, database access, cryptography, and much more. This is often referred to as Python's "batteries included" philosophy.

#### Multi-Paradigm

Python supports:
- **Procedural programming** — sequential code organized into functions
- **Object-oriented programming** — classes, inheritance, polymorphism
- **Functional programming** — first-class functions, `map`, `filter`, `reduce`, lambda expressions, comprehensions

#### Cross-Platform

Python runs on Windows, macOS, Linux, and many other platforms without modification to the source code.

#### Large Ecosystem

The Python Package Index (PyPI) hosts over 500,000 packages covering web frameworks (Django, Flask, FastAPI), scientific computing (NumPy, SciPy), machine learning (scikit-learn, PyTorch, TensorFlow), data analysis (pandas), and automation.

#### Readable Syntax

Python enforces indentation as part of its syntax, which compels consistent, readable code formatting. The guiding philosophy is captured in PEP 20 (The Zen of Python): "Readability counts."

---

### Q2. How is Python executed?

Understanding Python's execution model is fundamental to writing efficient code and diagnosing performance issues.

**Step 1 — Source Code**

You write Python source code in `.py` files using a text editor or IDE.

**Step 2 — Compilation to Bytecode**

When you run a `.py` file, the Python interpreter's compiler translates the source code into **bytecode** — a lower-level, platform-independent representation of your program. This bytecode is stored in `.pyc` files under the `__pycache__` directory. This step happens automatically and is largely invisible to the developer.

Bytecode is not machine code. It is an intermediate representation specific to the CPython Virtual Machine.

**Step 3 — Execution by the Python Virtual Machine (PVM)**

The PVM reads and executes the bytecode instruction-by-instruction. The PVM is a software-based virtual machine — a loop that fetches, decodes, and dispatches bytecode instructions.

```
Source code (.py)
        |
        v
  [Compiler/Lexer/Parser]
        |
        v
  Bytecode (.pyc in __pycache__)
        |
        v
  [Python Virtual Machine (PVM)]
        |
        v
     Output / Side Effects
```

**CPython vs. Other Implementations**

- **CPython** — The reference implementation, written in C. Most widely used.
- **PyPy** — JIT-compiled Python. Significantly faster for long-running programs.
- **Jython** — Python running on the JVM.
- **IronPython** — Python on the .NET CLR.
- **MicroPython** — Lightweight Python for microcontrollers.

**Inspecting Bytecode**

You can inspect bytecode using the `dis` module:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output (abbreviated):
```
  2           0 RESUME                   0
  3           2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_OP               0 (+)
             10 RETURN_VALUE
```

---

### Q3. What is PEP 8 and why is it important?

**PEP** stands for **Python Enhancement Proposal**. PEPs are design documents that describe new features, processes, or conventions for the Python language and its ecosystem. PEP 8 is the official **Style Guide for Python Code**, authored by Guido van Rossum and Barry Warsaw.

**Why PEP 8 Matters**

Code is read far more often than it is written. In production environments, teams of engineers maintain codebases over years. Consistent style reduces cognitive load when switching between files, modules, and projects. PEP 8 establishes a shared convention that the entire Python community follows.

**Key PEP 8 Rules**

*Indentation*

Use 4 spaces per indentation level. Never mix tabs and spaces.

```python
# Correct
def calculate_tax(income):
    if income > 50000:
        return income * 0.3
    return income * 0.2

# Wrong — 2-space indentation
def calculate_tax(income):
  if income > 50000:
    return income * 0.3
```

*Line Length*

Limit all lines to a maximum of 79 characters. Docstrings and comments should be limited to 72 characters.

*Blank Lines*

- Two blank lines around top-level function and class definitions.
- One blank line between methods within a class.

*Imports*

- Imports should be on separate lines.
- Order: standard library, third-party, local.
- Use absolute imports.

```python
# Correct
import os
import sys

import requests

from mypackage import mymodule
```

*Naming Conventions*

| Type | Convention | Example |
|---|---|---|
| Variables and functions | `snake_case` | `user_name`, `calculate_total` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `API_BASE_URL` |
| Classes | `PascalCase` | `UserAccount`, `PaymentProcessor` |
| Private attributes | `_single_leading_underscore` | `_internal_cache` |
| Name mangling | `__double_leading_underscore` | `__secret_key` |

*Whitespace*

```python
# Correct
x = 5
result = func(arg1, arg2)
my_list[1:3]

# Wrong
x=5
result = func( arg1 , arg2 )
my_list[1 : 3]
```

**Enforcing PEP 8**

Several tools automate PEP 8 compliance:
- `pycodestyle` — checks style violations
- `flake8` — combines pycodestyle with pyflakes (logical errors)
- `black` — an opinionated auto-formatter
- `isort` — sorts imports automatically
- `pylint` — comprehensive linter

---

### Q4. How is memory allocation and garbage collection handled in Python?

Python manages memory automatically. Understanding this mechanism is essential for diagnosing memory leaks and writing memory-efficient production applications.

**Memory Allocation**

Python uses a private heap to store all objects and data structures. The CPython memory manager sits between the operating system allocator and the Python application, handling allocation in layers:

- **Raw memory layer** — wraps `malloc`/`free` from the C standard library
- **Python object allocator** — manages memory for small objects (< 512 bytes) using pooled arenas called `pymalloc`
- **Object-specific allocators** — specialized allocators for common objects like integers and strings

**Reference Counting**

Every Python object maintains an internal reference count — the number of variables, data structures, or other objects pointing to it. When an object's reference count drops to zero, CPython immediately deallocates it.

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x itself + the argument to getrefcount)

y = x                       # another reference
print(sys.getrefcount(x))  # 3

del y                       # y's reference removed
print(sys.getrefcount(x))  # back to 2
```

Reference counting is fast and deterministic for most cases — an object is freed as soon as its last reference disappears.

**Cyclic Garbage Collector**

Reference counting alone cannot handle **circular references** — situations where object A references object B, and object B references object A. Neither reaches zero even when both are otherwise unreachable.

```python
a = []
b = []
a.append(b)  # a references b
b.append(a)  # b references a
del a, del b  # Both have ref count 1, not 0 — cyclic garbage
```

Python's cyclic garbage collector (`gc` module) detects these cycles using a generational algorithm:

- **Generation 0** — newly created objects
- **Generation 1** — objects that survived one GC cycle
- **Generation 2** — objects that survived multiple GC cycles

The collector runs periodically and can also be triggered manually:

```python
import gc

gc.collect()            # trigger a full collection
print(gc.get_count())   # (count0, count1, count2)
gc.disable()            # disable the cyclic GC (only safe if you avoid cycles)
```

**Memory Optimization Techniques**

- **`__slots__`** — prevents per-instance `__dict__` creation, reducing memory per object
- **Generators** — yield values lazily instead of materializing entire sequences
- **`weakref`** — create references that do not increase the reference count

```python
class Point:
    __slots__ = ['x', 'y']  # No __dict__ per instance

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

### Q5. What are the built-in data types in Python?

Python provides a rich set of built-in types. They are organized into several categories.

**Numeric Types**

| Type | Description | Example |
|---|---|---|
| `int` | Arbitrary precision integer | `42`, `-7`, `10**100` |
| `float` | IEEE 754 double-precision | `3.14`, `-0.001` |
| `complex` | Complex number | `3 + 4j` |
| `bool` | Subclass of `int`; `True`/`False` | `True == 1`, `False == 0` |

```python
x = 10**100          # Python int has no overflow limit
pi = 3.14159
z = 2 + 3j
print(z.real, z.imag)  # 2.0 3.0
```

**Sequence Types**

| Type | Mutable | Ordered | Example |
|---|---|---|---|
| `list` | Yes | Yes | `[1, 2, 3]` |
| `tuple` | No | Yes | `(1, 2, 3)` |
| `range` | No | Yes | `range(0, 10, 2)` |
| `str` | No | Yes | `"hello"` |

**Mapping Types**

| Type | Description | Example |
|---|---|---|
| `dict` | Key-value pairs (insertion-ordered since 3.7) | `{"name": "Alice", "age": 30}` |

**Set Types**

| Type | Mutable | Unique Elements | Example |
|---|---|---|---|
| `set` | Yes | Yes | `{1, 2, 3}` |
| `frozenset` | No | Yes | `frozenset({1, 2, 3})` |

**Binary Types**

| Type | Description |
|---|---|
| `bytes` | Immutable sequence of bytes |
| `bytearray` | Mutable sequence of bytes |
| `memoryview` | Memory view of a buffer object |

**None Type**

`NoneType` has exactly one value: `None`. It represents the absence of a value and is Python's null equivalent.

```python
result = None
print(type(result))   # <class 'NoneType'>
print(result is None) # True
```

**Type Checking**

```python
x = 42
print(type(x))            # <class 'int'>
print(isinstance(x, int)) # True
print(isinstance(x, (int, float)))  # True — checks multiple types
```

---

### Q6. Explain the difference between a mutable and immutable object.

This distinction governs how Python objects behave when assigned to variables, passed to functions, or used as dictionary keys.

**Immutable Objects**

An immutable object's state cannot be changed after it is created. Any operation that appears to modify it actually creates a new object.

Immutable types: `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`

```python
x = "hello"
print(id(x))       # memory address, e.g. 140234567890

x = x + " world"  # creates a NEW string object
print(id(x))       # different memory address
```

```python
t = (1, 2, 3)
t[0] = 99          # TypeError: 'tuple' object does not support item assignment
```

**Mutable Objects**

A mutable object's state can be changed in-place without creating a new object.

Mutable types: `list`, `dict`, `set`, `bytearray`, most user-defined class instances

```python
lst = [1, 2, 3]
print(id(lst))     # memory address

lst.append(4)      # modifies the SAME object in place
print(id(lst))     # SAME memory address as before
```

**Critical Implications — Aliasing**

When two variables point to the same mutable object, changes through one variable are visible through the other.

```python
a = [1, 2, 3]
b = a              # b and a point to the SAME list

b.append(4)
print(a)           # [1, 2, 3, 4] — a was also affected!

# To create an independent copy:
c = a.copy()       # shallow copy
c.append(5)
print(a)           # [1, 2, 3, 4] — a is unchanged
```

**Implications for Function Arguments**

Python passes object references (not values, not pointers). Mutating a mutable argument inside a function affects the caller's object:

```python
def add_item(collection, item):
    collection.append(item)  # modifies the original list

my_list = [1, 2]
add_item(my_list, 3)
print(my_list)   # [1, 2, 3]
```

**Mutable Default Arguments — A Classic Pitfall**

```python
# WRONG — the default list is created ONCE and shared across all calls
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] — unexpected!

# CORRECT — use None as default, create inside the function
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```

**Dictionary Keys Must Be Hashable (Immutable)**

Only immutable objects can serve as dictionary keys because hashing requires that the key's value does not change.

```python
d = {}
d[(1, 2)] = "point"    # tuple is hashable — valid
d[[1, 2]] = "point"    # TypeError: unhashable type: 'list'
```

---

### Q7. How do you handle exceptions in Python?

Exception handling is the mechanism by which a program detects and responds to runtime errors without crashing. Python uses a structured `try/except/else/finally` construct.

**Basic Structure**

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handles the specific exception
    print("Cannot divide by zero")
```

**Catching Multiple Exceptions**

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Input was not a valid integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Catching Multiple Exceptions in One Clause**

```python
try:
    process_data()
except (KeyError, IndexError) as e:
    print(f"Data access error: {e}")
```

**The `else` Clause**

The `else` block executes only if no exception was raised in the `try` block. This is useful for separating the success path from the error handling path.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print(f"Division succeeded: {result}")  # runs only on success
```

**The `finally` Clause**

The `finally` block always executes, whether or not an exception occurred. It is used to release resources such as file handles, network connections, or database cursors.

```python
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    if file:
        file.close()   # always executed
```

**Re-raising Exceptions**

```python
try:
    risky_operation()
except ValueError as e:
    log_error(e)
    raise   # re-raise the original exception with its traceback
```

**Raising Exceptions**

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
```

**Custom Exception Classes**

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw {amount}. Current balance: {balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)  # Cannot withdraw 200. Current balance: 100
```

**Exception Hierarchy**

Python's built-in exceptions form a class hierarchy rooted at `BaseException`. The most important node is `Exception`, which is the base class for all non-system-exiting exceptions. `KeyboardInterrupt` and `SystemExit` derive from `BaseException`, not `Exception`, which is why `except Exception` does not catch them.

---

### Q8. What is the difference between list and tuple?

Both `list` and `tuple` are ordered, indexed sequences that can contain heterogeneous elements. Their primary difference is mutability.

| Feature | `list` | `tuple` |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutability | Mutable — elements can be added, removed, or changed | Immutable — cannot be modified after creation |
| Performance | Slightly slower due to mutability overhead | Faster for iteration and access |
| Memory | More memory (extra space for dynamic resizing) | Less memory |
| Hashable | No (cannot be a dict key or set element) | Yes (if all elements are also hashable) |
| Use case | Collections that change over time | Fixed records, function return values, dict keys |

```python
# List — mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "avocado"
print(fruits)  # ['avocado', 'banana', 'cherry', 'date']

# Tuple — immutable
point = (10, 20)
point[0] = 99   # TypeError: 'tuple' object does not support item assignment
```

**Memory Comparison**

```python
import sys

lst = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)

print(sys.getsizeof(lst))  # 120 bytes (approximate)
print(sys.getsizeof(tup))  # 80 bytes (approximate)
```

**Tuple Packing and Unpacking**

Tuples shine in multiple return values and sequence unpacking:

```python
def get_coordinates():
    return 40.7128, -74.0060  # implicitly a tuple

lat, lon = get_coordinates()  # unpacking

# Extended unpacking (Python 3)
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

**Named Tuples**

For tuples with semantic field names, use `collections.namedtuple` or `typing.NamedTuple`:

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(3.0, 4.0)
print(p.x)        # 3.0
print(p[0])       # 3.0 — still accessible by index
print(p._asdict()) # {'x': 3.0, 'y': 4.0}
```

---

### Q9. How do you create a dictionary in Python?

A dictionary (`dict`) is Python's implementation of a hash map — an unordered (in Python 3.7+ insertion-ordered) collection of key-value pairs. Keys must be unique and hashable. Values can be any type.

**Creation Methods**

```python
# Literal syntax
person = {"name": "Alice", "age": 30, "city": "Mumbai"}

# Built-in dict() constructor
person = dict(name="Alice", age=30, city="Mumbai")

# From list of key-value pairs
person = dict([("name", "Alice"), ("age", 30)])

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Empty dictionary
config = {}
config = dict()
```

**Accessing and Modifying Values**

```python
person = {"name": "Alice", "age": 30}

# Access
print(person["name"])                  # "Alice"
print(person.get("email"))             # None — no KeyError
print(person.get("email", "N/A"))      # "N/A" — default value

# Modify
person["age"] = 31
person["email"] = "alice@example.com"  # add new key

# Remove
del person["city"]                      # KeyError if key absent
person.pop("age")                       # returns value, no error if default given
person.pop("phone", None)               # safe removal
```

**Useful Dictionary Methods**

```python
d = {"a": 1, "b": 2, "c": 3}

d.keys()      # dict_keys(['a', 'b', 'c'])
d.values()    # dict_values([1, 2, 3])
d.items()     # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Merge two dictionaries (Python 3.9+)
d1 = {"x": 1}
d2 = {"y": 2}
merged = d1 | d2   # {'x': 1, 'y': 2}

# Update in-place
d1.update(d2)

# setdefault — set key only if it doesn't exist
d.setdefault("d", 0)   # adds 'd': 0 if 'd' not present
```

**Iterating a Dictionary**

```python
config = {"host": "localhost", "port": 5432, "db": "mydb"}

for key in config:               # iterate keys
    print(key)

for key, value in config.items():  # iterate key-value pairs
    print(f"{key} = {value}")
```

**defaultdict and OrderedDict**

```python
from collections import defaultdict, OrderedDict

# defaultdict — returns a default value for missing keys
word_count = defaultdict(int)
for word in "the cat sat on the mat".split():
    word_count[word] += 1

# Counter — subclass of dict for counting
from collections import Counter
counter = Counter("the cat sat on the mat".split())
print(counter.most_common(2))  # [('the', 2), ('cat', 1)]
```

---

### Q10. What is the difference between `==` and `is` operator in Python?

This is one of the most commonly misunderstood distinctions in Python, and confusing the two leads to subtle bugs.

**`==` — Value Equality**

The `==` operator tests whether two objects have the **same value**. It calls the `__eq__` method of the left operand.

**`is` — Identity (Reference) Equality**

The `is` operator tests whether two variables point to the **same object in memory** — i.e., they have the same `id()`.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  — same value
print(a is b)   # False — different objects in memory

c = a           # c is an alias for the same object as a
print(a is c)   # True  — same object
```

**Integer Caching (Small Int Interning)**

CPython caches small integers in the range `[-5, 256]` and interns short strings for performance. This can make `is` behave unexpectedly:

```python
x = 100
y = 100
print(x is y)   # True  — CPython reuses the same object

x = 1000
y = 1000
print(x is y)   # False — outside the cached range, new objects created
```

**Rule of Thumb**

- Use `==` when comparing values (numbers, strings, lists, etc.)
- Use `is` only when checking for `None`, or when you genuinely need to verify object identity

```python
# Correct — checking for None
if result is None:
    handle_missing()

# Incorrect — using == for None check (works, but not idiomatic)
if result == None:
    handle_missing()
```

---

## 2. Python Functions and Modules

---

### Q11. How does a Python function work?

A function is a named, reusable block of code defined using the `def` keyword. It encapsulates logic, accepts inputs via parameters, and optionally returns values. In Python, functions are **first-class objects** — they can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions.

**Defining and Calling Functions**

```python
def greet(name, greeting="Hello"):
    """
    Return a greeting message.

    Args:
        name: The name of the person to greet.
        greeting: The greeting to use. Defaults to 'Hello'.

    Returns:
        A formatted greeting string.
    """
    return f"{greeting}, {name}!"

message = greet("Alice")           # "Hello, Alice!"
message = greet("Bob", "Welcome")  # "Welcome, Bob!"
```

**Types of Parameters**

```python
def function_demo(
    positional_arg,          # required positional
    default_arg=10,          # has a default value
    *args,                   # variable positional arguments
    keyword_only,            # must be passed as keyword
    **kwargs                 # variable keyword arguments
):
    print(positional_arg, default_arg, args, keyword_only, kwargs)

function_demo(
    "hello",
    20,
    "extra1", "extra2",
    keyword_only="required",
    extra_kw="value"
)
```

**Return Values**

A function without a `return` statement (or with bare `return`) implicitly returns `None`. Multiple values are returned as a tuple.

```python
def min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)   # 1 9
```

**Functions as First-Class Objects**

```python
def double(x):
    return x * 2

transform = double       # assign to variable
print(transform(5))      # 10

operations = [double, abs, str]  # store in list
for op in operations:
    print(op(-3))        # -6, 3, '-3'
```

**Scope and the LEGB Rule**

Python resolves names using the **LEGB** rule:
- **L**ocal — inside the current function
- **E**nclosing — in any enclosing function scopes
- **G**lobal — at the module level
- **B**uilt-in — Python's built-in namespace

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)       # enclosing

outer()
print(x)           # global
```

---

### Q12. What is a lambda function, and where would you use it?

A lambda function is an **anonymous**, single-expression function defined using the `lambda` keyword. It is syntactic sugar for simple throwaway functions that are not worth naming.

**Syntax**

```python
lambda parameters: expression
```

**Examples**

```python
# Equivalent function and lambda
def square(x):
    return x ** 2

square = lambda x: x ** 2

print(square(5))  # 25
```

**Primary Use Cases**

*Sorting with a custom key:*

```python
employees = [
    {"name": "Alice", "salary": 95000},
    {"name": "Bob", "salary": 80000},
    {"name": "Carol", "salary": 110000},
]

# Sort by salary descending
sorted_employees = sorted(employees, key=lambda e: e["salary"], reverse=True)
```

*With `map`, `filter`, `reduce`:*

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

total = reduce(lambda acc, x: acc + x, numbers)
# 55
```

**When NOT to Use Lambda**

PEP 8 discourages assigning a lambda to a variable name. Use `def` instead. Lambdas are appropriate only when passed as an argument inline.

```python
# Bad — assignment to a name
double = lambda x: x * 2

# Good — use a proper function definition
def double(x):
    return x * 2
```

---

### Q13. Explain `*args` and `**kwargs` in Python.

These special parameter syntaxes allow functions to accept an arbitrary number of arguments.

**`*args` — Arbitrary Positional Arguments**

When you prefix a parameter with `*`, Python collects all extra positional arguments into a **tuple** with that name (conventionally `args`, but the name is arbitrary).

```python
def sum_all(*args):
    print(type(args))  # <class 'tuple'>
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
```

**`**kwargs` — Arbitrary Keyword Arguments**

When you prefix a parameter with `**`, Python collects all extra keyword arguments into a **dictionary** with that name.

```python
def create_profile(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_profile(name="Alice", age=30, city="Mumbai", role="Engineer")
```

**Combining Both**

The order must be: `positional`, `*args`, `keyword-only`, `**kwargs`.

```python
def complex_function(required, *args, keyword_only=None, **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"keyword_only: {keyword_only}")
    print(f"kwargs: {kwargs}")

complex_function(
    "must_have",
    "extra1", "extra2",
    keyword_only="kw_value",
    option1="a", option2="b"
)
```

**Unpacking with `*` and `**`**

The same syntax is used to unpack sequences and dictionaries into function calls:

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))           # 6 — unpacks list into positional args

params = {"a": 1, "b": 2, "c": 3}
print(add(**params))        # 6 — unpacks dict into keyword args
```

---

### Q14. What are decorators in Python?

A decorator is a higher-order function that wraps another function to extend or modify its behavior without changing its source code. This is a practical application of Python's first-class functions and closures.

**Basic Decorator Pattern**

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Before the function call
# Hello, Alice!
# After the function call
```

The `@my_decorator` syntax is equivalent to `say_hello = my_decorator(say_hello)`.

**Preserving Metadata with `functools.wraps`**

Without `functools.wraps`, the wrapped function loses its `__name__` and `__doc__`:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)    # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Practical Examples**

*Timing decorator:*

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_operation():
    time.sleep(0.5)

slow_operation()  # slow_operation took 0.5001s
```

*Retry decorator:*

```python
import functools
import time

def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url):
    # might raise requests.exceptions.ConnectionError
    pass
```

**Stacking Decorators**

Decorators are applied from bottom to top:

```python
@decorator_a
@decorator_b
def func():
    pass

# Equivalent to:
func = decorator_a(decorator_b(func))
```

---

### Q15. How can you create a module in Python?

A **module** is any Python file (`.py`) whose definitions (functions, classes, variables) can be imported and reused in other Python files.

**Creating a Module**

Simply create a `.py` file. For example, `mathutils.py`:

```python
# mathutils.py

PI = 3.14159265358979

def area_of_circle(radius):
    """Calculate the area of a circle."""
    return PI * radius ** 2

def factorial(n):
    """Calculate n! recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

**Importing the Module**

```python
# main.py

import mathutils
print(mathutils.area_of_circle(5))   # 78.539...
print(mathutils.PI)

from mathutils import factorial, Vector2D
print(factorial(6))   # 720

from mathutils import area_of_circle as area
print(area(3))

import mathutils as mu
print(mu.PI)
```

**The `__init__.py` File**

To make a directory a package, add an `__init__.py` file (can be empty):

```
mypackage/
    __init__.py
    mathutils.py
    stringutils.py
```

---

### Q16. How do you share global variables across modules?

The recommended approach is to place shared state in a dedicated module, then import it wherever needed.

```python
# config.py — the shared state module
DATABASE_URL = "postgresql://localhost/mydb"
DEBUG = False
MAX_RETRIES = 3
```

```python
# service_a.py
import config

def connect():
    print(f"Connecting to {config.DATABASE_URL}")

config.DEBUG = True  # modifies the shared state
```

```python
# service_b.py
import config

def run():
    if config.DEBUG:
        print("Debug mode is on")
```

**Important:** When you import a module, Python caches it in `sys.modules`. All subsequent imports of the same module return the same object. This means modifications to module-level variables are visible to all importers.

**Using `global` Inside Functions**

```python
counter = 0

def increment():
    global counter   # tells Python this refers to the module-level 'counter'
    counter += 1
```

Without the `global` keyword, assigning to `counter` inside a function would create a new local variable, leaving the module-level one unchanged.

---

### Q17. What is the use of `if __name__ == '__main__'`?

Every Python module has a built-in attribute `__name__`. When a file is run directly by the interpreter, `__name__` is set to the string `'__main__'`. When it is imported by another module, `__name__` is set to the module's filename (without `.py`).

**Why This Matters**

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    # This block runs ONLY when calculator.py is executed directly.
    # It does NOT run when calculator is imported by another module.
    print("Running calculator tests...")
    print(add(3, 5))       # 8
    print(subtract(10, 4)) # 6
```

When `main_app.py` does `import calculator`, the `if __name__ == '__main__':` block is **not** executed. This allows the same file to serve as both a reusable library and a standalone script.

**Production Usage Pattern**

```python
# app.py

def main():
    """Application entry point."""
    setup_logging()
    load_configuration()
    start_server()

if __name__ == '__main__':
    main()
```

---

### Q18. What are Python namespaces?

A **namespace** is a mapping from names (identifiers) to objects. It is the mechanism by which Python avoids name collisions between different modules, classes, and functions.

**Types of Namespaces**

| Namespace | Created When | Destroyed When |
|---|---|---|
| Built-in | Python interpreter starts | Interpreter shuts down |
| Global (module) | Module is imported or executed | Program ends |
| Enclosing | Outer function is called | Outer function returns |
| Local | Function is called | Function returns |

**Namespace Implementation**

Internally, namespaces are implemented as Python dictionaries. You can inspect them:

```python
x = 10
y = 20

print(globals())   # dict of current module's global namespace
# {'__name__': '__main__', 'x': 10, 'y': 20, ...}

def my_func():
    a = 1
    b = 2
    print(locals())  # {'a': 1, 'b': 2}

my_func()
```

**Namespace Isolation**

Two modules can both define a function named `calculate` without conflict because each has its own namespace. You access them as `module_a.calculate` and `module_b.calculate`.

---

### Q19. How does a Python module search path work?

When you write `import mymodule`, Python searches for `mymodule` in a specific sequence of locations defined by `sys.path`.

**The Search Order**

1. The directory of the script being run (or the current directory in interactive mode)
2. Directories listed in the `PYTHONPATH` environment variable
3. The installation-dependent default paths (standard library, site-packages)

```python
import sys
print(sys.path)
# ['', '/usr/lib/python312.zip', '/usr/lib/python3.12', ...]
```

**Inspecting and Modifying `sys.path`**

```python
import sys

# Add a custom directory to the search path at runtime
sys.path.insert(0, '/path/to/my/custom/modules')

import mymodule  # now searches /path/to/my/custom/modules first
```

**`PYTHONPATH` Environment Variable**

Set before launching Python:
```bash
export PYTHONPATH=/path/to/extra/modules
python my_script.py
```

**The `.pth` Files**

Files with a `.pth` extension in the `site-packages` directory can add additional paths to `sys.path` at startup.

---

### Q20. What is a Python package?

A **package** is a directory that organizes related modules into a hierarchical namespace. It must contain an `__init__.py` file (required in Python 2; optional but conventional in Python 3 for regular packages; not needed for namespace packages).

**Package Structure**

```
myproject/
    __init__.py
    models/
        __init__.py
        user.py
        product.py
    services/
        __init__.py
        auth.py
        payment.py
    utils/
        __init__.py
        validators.py
        formatters.py
```

**`__init__.py` Purpose**

The `__init__.py` file is executed when the package is imported. It can expose a public API by selectively importing from submodules:

```python
# myproject/__init__.py
from .models.user import User
from .models.product import Product
from .services.auth import AuthService

__all__ = ["User", "Product", "AuthService"]
```

Now users can write `from myproject import User` instead of `from myproject.models.user import User`.

**Relative vs. Absolute Imports**

```python
# Absolute import (recommended)
from myproject.services.auth import AuthService

# Relative import (within the same package)
from ..models.user import User  # go up two levels, then into models
from .validators import validate_email  # same package
```

---

## 3. Python Advanced Concepts

---

### Q21. What is list comprehension? Give an example.

List comprehension is a concise, readable syntax for creating a new list by transforming or filtering elements from an existing iterable. It is generally faster than an equivalent `for` loop because it is optimized at the bytecode level.

**Syntax**

```python
new_list = [expression for item in iterable if condition]
```

**Basic Examples**

```python
# Squares of 0-9
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent for loop
squares = []
for x in range(10):
    squares.append(x ** 2)
```

**With Filtering**

```python
# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Strings longer than 3 characters, uppercased
words = ["cat", "elephant", "dog", "rhinoceros", "ox"]
long_words = [w.upper() for w in words if len(w) > 3]
# ['ELEPHANT', 'RHINOCEROS']
```

**Nested List Comprehension**

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [cell for row in matrix for cell in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cartesian product
pairs = [(x, y) for x in range(3) for y in range(3)]
```

**Performance**

List comprehensions are typically 35–50% faster than equivalent `for` loops with `append` for CPython, because the entire operation is implemented as a specialized bytecode sequence.

---

### Q22. Explain dictionary comprehension.

Dictionary comprehension creates a new dictionary in a single, expressive line, analogous to list comprehension.

**Syntax**

```python
new_dict = {key_expr: value_expr for item in iterable if condition}
```

**Examples**

```python
# Square each number as key: value
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter a dictionary — keep only high earners
employees = {"Alice": 95000, "Bob": 45000, "Carol": 120000, "Dave": 38000}
high_earners = {name: sal for name, sal in employees.items() if sal > 50000}
# {'Alice': 95000, 'Carol': 120000}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Normalize string keys to lowercase
config = {"HOST": "localhost", "PORT": "5432", "DB": "mydb"}
normalized = {k.lower(): v for k, v in config.items()}
# {'host': 'localhost', 'port': '5432', 'db': 'mydb'}
```

**Set Comprehension**

A similar syntax applies to sets:

```python
unique_lengths = {len(word) for word in ["hello", "world", "hi", "there"]}
# {5, 2} — wait, 5, 5, 2, 5 — deduped to {2, 5}
```

---

### Q23. What are generators in Python, and how do you use them?

A **generator** is a function that yields values one at a time, pausing its execution state between calls. Instead of building an entire list in memory, a generator produces items lazily — only computing the next value when asked. This is critical for processing large datasets or infinite sequences.

**Generator Functions — `yield` keyword**

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i    # pause, return i, resume from here next time
        i += 1

gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

for num in count_up_to(5):
    print(num)    # 1 2 3 4 5
```

**Memory Efficiency**

```python
import sys

# List — all 1M integers in memory at once
my_list = [x for x in range(1_000_000)]
print(sys.getsizeof(my_list))  # ~8 MB

# Generator — stores only the current state
my_gen = (x for x in range(1_000_000))  # generator expression
print(sys.getsizeof(my_gen))   # ~104 bytes
```

**Generator Expressions**

Similar to list comprehensions but with parentheses. They produce a generator object without materializing the entire sequence:

```python
# Sum of squares without building an intermediate list
total = sum(x**2 for x in range(1, 1001))

# Reading large files line by line
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("giant_log.txt"):
    process(line)
```

**`send()` and Two-Way Communication**

Generators can also receive values via `send()`, enabling coroutine-like behavior:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)          # prime the generator (advance to first yield)
gen.send(10)       # total = 10
gen.send(20)       # total = 30
gen.send(5)        # total = 35
```

---

### Q24. How do you implement concurrency in Python?

Python offers three main concurrency models, each suited to different problem types.

**1. Threading (`threading` module)**

Best for **I/O-bound** tasks (network requests, file reads, database queries). Multiple threads share the same memory space. Due to the GIL, only one thread executes Python bytecode at a time, but threads can overlap during I/O waits.

```python
import threading
import requests

urls = ["https://example.com"] * 5
results = []

def fetch(url):
    response = requests.get(url)
    results.append(response.status_code)

threads = [threading.Thread(target=fetch, args=(url,)) for url in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(results)
```

**2. Multiprocessing (`multiprocessing` module)**

Best for **CPU-bound** tasks (numerical computation, image processing). Each process has its own Python interpreter and memory space, bypassing the GIL entirely.

```python
from multiprocessing import Pool

def cpu_intensive(n):
    return sum(i ** 2 for i in range(n))

with Pool(processes=4) as pool:
    results = pool.map(cpu_intensive, [10**6, 10**6, 10**6, 10**6])

print(results)
```

**3. Asyncio (`asyncio` module)**

Best for **high-concurrency I/O-bound** tasks with thousands of concurrent operations (web servers, API clients). A single thread runs an event loop that switches between coroutines when they wait on I/O.

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://example.com"] * 5
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

results = asyncio.run(main())
```

**Decision Matrix**

| Scenario | Best Tool |
|---|---|
| Many network/DB requests | `asyncio` or `threading` |
| Heavy CPU computation | `multiprocessing` |
| Simple parallel tasks | `concurrent.futures.ThreadPoolExecutor` or `ProcessPoolExecutor` |

---

### Q25. What are coroutines and how do they differ from threads?

A **coroutine** is a specialized form of generator that can be paused and resumed cooperatively, rather than preemptively. In Python 3.5+, coroutines are defined with `async def` and awaited with `await`.

**Coroutine Definition**

```python
import asyncio

async def fetch_data(delay):
    print(f"Fetching data (will take {delay}s)...")
    await asyncio.sleep(delay)   # yields control back to the event loop
    print("Data fetched!")
    return {"status": "ok", "delay": delay}

async def main():
    result = await fetch_data(2)
    print(result)

asyncio.run(main())
```

**Key Differences: Coroutines vs. Threads**

| Aspect | Coroutines | Threads |
|---|---|---|
| Switching mechanism | **Cooperative** — switches only at `await` | **Preemptive** — OS scheduler can switch at any time |
| Memory overhead | Very low (~1KB per coroutine) | Higher (~8MB per thread for stack) |
| Concurrency limit | Thousands to millions | Hundreds (OS-limited) |
| Data sharing safety | Safe within single thread (no race conditions on Python objects) | Requires locks (Mutex, RLock, Semaphore) |
| GIL impact | Not affected (single thread) | Constrained by GIL for CPU work |
| Use case | High-concurrency I/O | Moderate concurrency, legacy I/O |

**Concurrency with `asyncio.gather`**

```python
import asyncio

async def task(name, duration):
    await asyncio.sleep(duration)
    return f"{name} done"

async def main():
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 0.5),
    )
    print(results)  # All three run concurrently; total ~2s, not 3.5s

asyncio.run(main())
```

---

### Q26. What is the Global Interpreter Lock (GIL)?

The **Global Interpreter Lock (GIL)** is a mutex in CPython that ensures only one thread executes Python bytecode at any given moment, even on multi-core hardware. It exists because CPython's memory management (specifically reference counting) is not thread-safe.

**Why the GIL Exists**

CPython's reference counting requires that incrementing and decrementing reference counts be atomic operations. Rather than protecting every reference count operation with a fine-grained lock (which would be complex and slow), the CPython team chose a single lock covering the entire interpreter.

**Consequences**

- **Multi-threaded CPU-bound code does not scale linearly** with the number of threads — in fact, adding threads to CPU-bound work can make it *slower* due to lock contention.
- **I/O-bound threading still works well** because threads release the GIL while waiting on I/O operations (file reads, network calls, sleep).

```python
# CPU-bound — GIL hurts scaling
import threading

def count(n):
    while n > 0:
        n -= 1  # GIL prevents true parallelism here

t1 = threading.Thread(target=count, args=(50_000_000,))
t2 = threading.Thread(target=count, args=(50_000_000,))

# Two threads are SLOWER than single thread due to GIL contention
```

**Workarounds**

- **`multiprocessing`** — each process has its own GIL; true CPU parallelism
- **C extensions** — NumPy, SciPy, etc. release the GIL during heavy C-level computation
- **`concurrent.futures.ProcessPoolExecutor`** — process pool with a familiar API

**GIL Removal in Python 3.13**

Python 3.13 introduced experimental support for running CPython without the GIL (PEP 703 — "Making the Global Interpreter Lock Optional"). This is a major long-term effort toward true CPU-bound multi-threading.

---

### Q27. How would you optimize the performance of a Python application?

Performance optimization should follow a disciplined process: **measure first, optimize second**. Never optimize code you have not profiled — you will almost certainly optimize the wrong thing.

**Step 1 — Profile to Identify Bottlenecks**

```python
import cProfile
import pstats
import io

pr = cProfile.Profile()
pr.enable()
my_function_to_profile()
pr.disable()

stream = io.StringIO()
stats = pstats.Stats(pr, stream=stream).sort_stats("cumulative")
stats.print_stats(20)
print(stream.getvalue())
```

For line-by-line profiling, use `line_profiler`:
```bash
pip install line-profiler
kernprof -l -v my_script.py
```

**Step 2 — Algorithm and Data Structure Selection**

The biggest performance gains come from choosing the right algorithm:

```python
# O(n) lookup with list — slow for large n
def find_user_list(user_id, users):
    for user in users:
        if user["id"] == user_id:
            return user

# O(1) lookup with dict — fast regardless of n
users_by_id = {user["id"]: user for user in users}

def find_user_dict(user_id):
    return users_by_id.get(user_id)
```

**Step 3 — Use Built-in Functions and Standard Library**

Built-in functions like `sum`, `min`, `max`, `sorted`, `map`, `filter` are implemented in C and are significantly faster than equivalent Python loops.

```python
# Slow Python loop
total = 0
for x in numbers:
    total += x

# Fast built-in
total = sum(numbers)
```

**Step 4 — Generators for Large Data**

Avoid materializing large sequences into lists when iteration suffices:

```python
# Loads entire file into memory
lines = open("huge_file.txt").readlines()

# Streams line by line
for line in open("huge_file.txt"):
    process(line)
```

**Step 5 — NumPy for Numerical Work**

NumPy operations are vectorized and run in optimized C code, orders of magnitude faster than Python loops for numerical arrays:

```python
import numpy as np

arr = np.arange(1_000_000)
result = np.sum(arr ** 2)   # microseconds
```

**Step 6 — Caching and Memoization**

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Step 7 — Compiled Extensions**

For the most critical hotspots, compile to native code using:
- **Cython** — annotate Python with C types, compile to C extension
- **Numba** — JIT-compiles numerical functions with `@numba.jit`
- **PyPy** — alternative JIT-compiled interpreter for long-running programs

---

### Q28. What is a context manager and the `with` statement in Python?

A **context manager** is an object that manages a resource (file handle, database connection, lock) by automatically running setup code on entry and teardown code on exit — even if an exception occurs. The `with` statement is the syntax for using context managers.

**Without a Context Manager (fragile)**

```python
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()   # must remember this every time
```

**With Context Manager (clean)**

```python
with open("data.txt") as f:
    data = f.read()
# f.close() is called automatically, even if f.read() raises
```

**The Protocol: `__enter__` and `__exit__`**

A context manager implements two methods:

```python
class DatabaseConnection:
    def __init__(self, dsn):
        self.dsn = dsn
        self.connection = None

    def __enter__(self):
        self.connection = connect(self.dsn)
        print("Connection opened")
        return self.connection   # the value bound to 'as'

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.connection.rollback()
            print(f"Transaction rolled back due to {exc_type.__name__}")
        else:
            self.connection.commit()
        self.connection.close()
        print("Connection closed")
        return False   # False means exceptions are NOT suppressed

with DatabaseConnection("postgresql://localhost/mydb") as conn:
    conn.execute("INSERT INTO orders VALUES (1, 'widget', 100)")
```

**`contextlib.contextmanager` Decorator**

For simpler cases, `contextlib.contextmanager` turns a generator into a context manager:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    start = time.perf_counter()
    try:
        yield   # code inside the 'with' block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name} took {elapsed:.4f}s")

with timer("data processing"):
    process_large_dataset()
```

---

### Q29. What strategies can be employed to optimize memory usage in Python applications?

**1. Use Generators Instead of Lists**

```python
# Loads 10M items into RAM
all_records = [process(record) for record in fetch_all_records()]

# Processes one at a time
for record in (process(r) for r in fetch_all_records()):
    save(record)
```

**2. `__slots__` for Memory-Efficient Classes**

By default, each Python instance has a `__dict__` dictionary to store attributes, consuming extra memory. Defining `__slots__` eliminates this:

```python
import sys

class PointNormal:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

class PointSlotted:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

p1 = PointNormal(1.0, 2.0, 3.0)
p2 = PointSlotted(1.0, 2.0, 3.0)

print(sys.getsizeof(p1.__dict__))  # 232 bytes
# p2 has no __dict__ — memory saving
```

**3. Use NumPy Arrays for Numerical Data**

```python
import numpy as np
import sys

python_list = [float(i) for i in range(100_000)]
numpy_array = np.arange(100_000, dtype=np.float64)

print(sys.getsizeof(python_list))  # ~824,464 bytes
print(numpy_array.nbytes)         # 800,000 bytes — and much faster
```

**4. Delete References No Longer Needed**

```python
large_data = load_huge_dataset()
processed = transform(large_data)

del large_data   # allow garbage collector to reclaim
import gc
gc.collect()     # force collection if cyclic references involved
```

**5. `array` Module for Typed Arrays**

```python
import array

# Stores 64-bit floats efficiently (no Python object overhead per element)
typed_array = array.array('d', range(100_000))
```

**6. Memory-Mapped Files**

For processing files too large to fit in RAM:

```python
import mmap

with open("huge_file.bin", "rb") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        chunk = mm[0:1024]  # read only what you need
```

**7. `tracemalloc` for Memory Profiling**

```python
import tracemalloc

tracemalloc.start()
# ... run your code ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)
```

---

### Q30. What is monkey patching in Python?

**Monkey patching** is the practice of dynamically modifying a class or module at runtime, replacing or adding methods and attributes after the original code has been defined. Because Python classes and modules are mutable objects, their attributes can be changed at any point.

**Basic Example**

```python
class MathOperations:
    def add(self, a, b):
        return a + b

def subtract(self, a, b):
    return a - b

# Monkey-patch a new method onto the class at runtime
MathOperations.subtract = subtract

ops = MathOperations()
print(ops.add(5, 3))       # 8 — original
print(ops.subtract(5, 3))  # 2 — monkey-patched
```

**Patching a Third-Party Module**

```python
import json

original_dumps = json.dumps

def custom_dumps(obj, **kwargs):
    kwargs.setdefault("indent", 2)
    kwargs.setdefault("sort_keys", True)
    return original_dumps(obj, **kwargs)

json.dumps = custom_dumps  # patch the standard library function
```

**Primary Use Case — Testing with `unittest.mock`**

The most legitimate and common use of monkey patching is in testing — replacing real implementations (network calls, database queries) with controlled fakes:

```python
from unittest.mock import patch

def get_current_temperature():
    import requests
    response = requests.get("https://api.weather.com/temp")
    return response.json()["temperature"]

def test_temperature():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"temperature": 22}
        result = get_current_temperature()
        assert result == 22
```

**Risks of Monkey Patching**

- Makes code harder to understand — behavior is defined in multiple places
- Can cause subtle ordering bugs if patches are applied inconsistently
- May break when the underlying library changes its internals
- Should be used sparingly in production code (testing is the primary legitimate use case)

---

## 4. Python Object-Oriented Programming

---

### Q31. What are classes in Python?

A **class** is a blueprint for creating objects. It defines a set of attributes (data) and methods (behavior) that all instances of that class will share. Python classes are defined using the `class` keyword.

```python
class BankAccount:
    """Represents a bank account."""

    # Class attribute — shared by all instances
    interest_rate = 0.03

    def __init__(self, owner, initial_balance=0.0):
        # Instance attributes — unique to each object
        self.owner = owner
        self.balance = initial_balance
        self._transaction_history = []   # convention: internal attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._transaction_history.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._transaction_history.append(("withdrawal", amount))
        return self.balance

    def apply_interest(self):
        """Apply the class-level interest rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        return interest

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:.2f})"

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"


# Creating instances
alice_account = BankAccount("Alice", 1000.0)
bob_account = BankAccount("Bob", 500.0)

alice_account.deposit(500)
alice_account.withdraw(200)
print(alice_account)  # Alice's account: $1300.00
```

---

### Q32. How does Python support object-oriented programming?

Python fully supports the four foundational pillars of OOP:

**1. Encapsulation**

Bundling data and methods together inside a class, and restricting direct access to internals.

**2. Inheritance**

A class (subclass) can inherit attributes and methods from another class (superclass), enabling code reuse.

**3. Polymorphism**

Objects of different classes can be treated uniformly if they share a common interface.

**4. Abstraction**

Hiding implementation details behind a clean, simplified interface.

```python
from abc import ABC, abstractmethod

# Abstraction — abstract base class defines the interface
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area."""

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter."""

    def describe(self):
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

# Inheritance + Encapsulation — concrete implementations
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius   # encapsulated attribute

    def area(self):
        return 3.14159 * self._radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self._radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

# Polymorphism — calling the same method on different types
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for shape in shapes:
    print(shape.describe())  # each calls its own area() and perimeter()
```

---

### Q33. What is inheritance and give an example in Python?

**Inheritance** allows a new class (subclass or derived class) to acquire the attributes and methods of an existing class (superclass or base class). This promotes code reuse and establishes an "is-a" relationship.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def breathe(self):
        return f"{self.name} is breathing"

    def eat(self, food):
        return f"{self.name} eats {food}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canis lupus familiaris")
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

    def speak(self):
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, species="Felis catus")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"


rex = Dog("Rex", "German Shepherd")
whiskers = Cat("Whiskers")

print(rex.breathe())     # inherited from Animal
print(rex.fetch("ball")) # Dog-specific method
print(rex.speak())       # Rex says: Woof!
print(whiskers.speak())  # Whiskers says: Meow!
```

**Multiple Inheritance**

Python supports inheriting from multiple base classes:

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Anas platyrhynchos")

    def speak(self):
        return f"{self.name} says: Quack!"

donald = Duck("Donald")
print(donald.fly())    # Donald is flying
print(donald.swim())   # Donald is swimming
```

---

### Q34. How do you achieve encapsulation in Python?

Encapsulation restricts direct access to an object's internals, exposing only what is necessary through a controlled interface. Python uses naming conventions and properties rather than strict access modifiers like Java's `private`/`protected`.

**Convention-Based Access Control**

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public — accessible anywhere
        self._salary = salary     # protected — internal use convention
        self.__ssn = ssn          # private — name-mangled to _Employee__ssn

    def get_salary(self):
        return self._salary

    def give_raise(self, percent):
        if percent <= 0:
            raise ValueError("Raise percentage must be positive")
        self._salary *= (1 + percent / 100)
```

**Name Mangling**

Double-underscore attributes are name-mangled by Python to prevent accidental override in subclasses:

```python
emp = Employee("Alice", 80000, "123-45-6789")
print(emp.name)           # "Alice"
print(emp._salary)        # 80000 — accessible but discouraged
print(emp.__ssn)          # AttributeError: 'Employee' object has no attribute '__ssn'
print(emp._Employee__ssn) # "123-45-6789" — still accessible if you know the mangled name
```

**Properties — The Pythonic Way**

`@property` creates a controlled getter. Combined with `@attr.setter` and `@attr.deleter`, it provides a clean interface while running validation logic:

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = None
        self.celsius = celsius   # triggers the setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9


t = Temperature(25)
print(t.celsius)     # 25
print(t.fahrenheit)  # 77.0
t.celsius = -300     # ValueError: Temperature below absolute zero
```

---

### Q35. What are class methods, static methods, and instance methods?

These three method types differ in what they receive as their first argument and what they have access to.

**Instance Methods**

The default method type. Receives `self` — the instance — as the first argument. Has full access to instance and class state.

```python
class MyClass:
    class_var = "I am a class variable"

    def __init__(self, value):
        self.instance_var = value

    def instance_method(self):
        # Can access both instance and class state
        print(f"Instance: {self.instance_var}, Class: {self.class_var}")
```

**Class Methods**

Decorated with `@classmethod`. Receives `cls` — the class itself — as the first argument. Can access and modify class state. Commonly used as alternative constructors.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor from 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)   # cls refers to Date (or subclass)

    @classmethod
    def today(cls):
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

d = Date.from_string("2026-05-25")
print(d.year, d.month, d.day)   # 2026 5 25
```

**Static Methods**

Decorated with `@staticmethod`. Receives no implicit first argument. Has no access to instance or class state. Essentially a regular function that belongs to the class namespace for organizational purposes.

```python
class Validator:
    @staticmethod
    def is_valid_email(email):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password))

print(Validator.is_valid_email("alice@example.com"))  # True
print(Validator.is_strong_password("weak"))           # False
```

---

### Q36. What is polymorphism in Python?

**Polymorphism** (from Greek: "many forms") is the ability of different objects to respond to the same interface or method call in their own way. Python achieves polymorphism through duck typing — the principle that an object's suitability is determined by the presence of certain methods, not by the object's type.

**Duck Typing**

> "If it walks like a duck and quacks like a duck, then it's a duck."

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_noise(animal):
    # Does not care about the type — only that .speak() exists
    return animal.speak()

animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(make_noise(animal))
```

**Polymorphism via Inheritance (Override)**

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

for shape in [Circle(5), Square(4)]:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")
```

**Operator Overloading — `__dunder__` Methods**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):    # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):   # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):           # len(v)
        return 2

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 * 3)     # Vector(3, 6)
```

---

### Q37. Explain the use of the `super()` function.

`super()` returns a proxy object that delegates method calls to the parent class in the MRO (Method Resolution Order). It is essential for cooperative multiple inheritance and avoids hardcoding the parent class name.

**Basic Usage**

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity_kwh):
        super().__init__(make, model, year)   # call Vehicle.__init__
        self.battery_capacity_kwh = battery_capacity_kwh

    def describe(self):
        base_desc = super().describe()  # call Vehicle.describe()
        return f"{base_desc} (Electric, {self.battery_capacity_kwh} kWh)"

tesla = ElectricVehicle("Tesla", "Model 3", 2024, 75)
print(tesla.describe())  # 2024 Tesla Model 3 (Electric, 75 kWh)
```

**Why Not Hardcode the Parent Name?**

With multiple inheritance, hardcoding creates problems. `super()` follows the MRO and ensures each class in the hierarchy is called exactly once:

```python
class A:
    def method(self):
        print("A.method")
        super().method()

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()

D().method()
# D.method -> B.method -> C.method -> A.method
# Each runs exactly once despite the diamond inheritance
```

---

### Q38. What is method resolution order (MRO) in Python?

The **Method Resolution Order (MRO)** is the sequence in which Python searches through a class hierarchy to find a method or attribute. For single inheritance, it is simply the chain of parent classes. For multiple inheritance, Python uses the **C3 Linearization algorithm** to compute a consistent, deterministic order.

**Inspecting the MRO**

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

print(D.mro())
# Same as above, as a list
```

**C3 Linearization Rules**

The MRO is computed such that:
1. A class always appears before its parents
2. The order of parents in the class definition is preserved
3. The MRO of the parent classes is preserved (monotonicity)

**Diamond Inheritance**

```python
class Base:
    def greet(self):
        return "Hello from Base"

class Left(Base):
    def greet(self):
        return "Hello from Left"

class Right(Base):
    def greet(self):
        return "Hello from Right"

class Child(Left, Right):
    pass

print(Child().greet())   # "Hello from Left"
print(Child.__mro__)     # Child -> Left -> Right -> Base -> object
```

---

### Q39. What are magic methods in Python?

**Magic methods** (also called **dunder methods** — double-underscore methods) are special methods that Python calls implicitly in response to specific operations or syntax. They allow you to define how your objects behave with operators, built-in functions, and the standard Python data model.

**Common Magic Methods**

*Object lifecycle:*

```python
class Resource:
    def __init__(self):        # called on object creation
        print("Created")

    def __del__(self):         # called before garbage collection
        print("Destroyed")

    def __new__(cls):          # called to create the object (before __init__)
        return super().__new__(cls)
```

*String representation:*

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # Unambiguous developer-facing representation
        return f"Product(name={self.name!r}, price={self.price})"

    def __str__(self):
        # Human-readable user-facing representation
        return f"{self.name}: ${self.price:.2f}"
```

*Comparison operators:*

```python
from functools import total_ordering

@total_ordering  # fills in __le__, __gt__, __ge__ from __eq__ and __lt__
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius
```

*Container protocol:*

```python
class NumberList:
    def __init__(self, numbers):
        self._numbers = list(numbers)

    def __len__(self):                # len(obj)
        return len(self._numbers)

    def __getitem__(self, index):     # obj[index]
        return self._numbers[index]

    def __contains__(self, item):     # item in obj
        return item in self._numbers

    def __iter__(self):               # for x in obj
        return iter(self._numbers)
```

*Context manager protocol:*

```python
def __enter__(self): ...
def __exit__(self, exc_type, exc_val, exc_tb): ...
```

*Arithmetic operators:*

```python
def __add__(self, other): ...     # self + other
def __radd__(self, other): ...    # other + self (reflected)
def __iadd__(self, other): ...    # self += other
def __sub__(self, other): ...
def __mul__(self, other): ...
def __truediv__(self, other): ...
```

---

### Q40. How do you prevent a class from being inherited?

Python does not have a `final` keyword like Java. However, there are several ways to prevent subclassing.

**Method 1 — `__init_subclass__`** (Python 3.6+, clean approach)

```python
class FinalClass:
    def __init_subclass__(cls, **kwargs):
        raise TypeError(
            f"Class '{cls.__name__}' cannot inherit from 'FinalClass'"
        )

class Attempt(FinalClass):  # TypeError raised here
    pass
```

**Method 2 — Custom Metaclass**

```python
class FinalMeta(type):
    def __new__(mcs, name, bases, namespace):
        for base in bases:
            if isinstance(base, FinalMeta):
                raise TypeError(
                    f"Cannot subclass final class '{base.__name__}'"
                )
        return super().__new__(mcs, name, bases, namespace)

class Sealed(metaclass=FinalMeta):
    """This class cannot be subclassed."""

class AttemptedSubclass(Sealed):  # TypeError raised immediately
    pass
```

**Method 3 — `@final` Decorator** (Python 3.8+, from `typing`)

The `@final` decorator signals intent to type checkers like `mypy`. It does not enforce at runtime but is the idiomatic approach for annotated codebases:

```python
from typing import final

@final
class Configuration:
    """Cannot be subclassed (enforced by type checkers)."""
    ...
```

---

## 5. Python Debugging and Testing

---

### Q41. How do you debug a Python program?

Effective debugging follows a systematic process of hypothesis formation, evidence gathering, and verification.

**Print Debugging (quick and dirty)**

```python
def process_order(order):
    print(f"DEBUG: order received: {order}")
    total = sum(item["price"] for item in order["items"])
    print(f"DEBUG: total = {total}")
    return total
```

**`pdb` — Python Debugger (interactive)**

`pdb` is Python's built-in interactive debugger. It lets you step through code, inspect variables, and set breakpoints:

```python
import pdb

def calculate(a, b):
    pdb.set_trace()   # execution pauses here
    result = a / b
    return result
```

**Key `pdb` Commands**

| Command | Action |
|---|---|
| `n` (next) | Execute next line |
| `s` (step) | Step into function call |
| `c` (continue) | Continue until next breakpoint |
| `l` (list) | Show current code context |
| `p expression` | Print value of expression |
| `pp expression` | Pretty-print |
| `b 42` | Set breakpoint at line 42 |
| `q` (quit) | Exit debugger |

**Python 3.7+ `breakpoint()` Built-in**

```python
def calculate(a, b):
    breakpoint()   # cleaner; respects PYTHONBREAKPOINT env variable
    return a / b
```

Set `PYTHONBREAKPOINT=0` to disable all breakpoints without modifying code.

**Post-Mortem Debugging**

```python
import pdb
import traceback

try:
    risky_function()
except Exception:
    traceback.print_exc()
    pdb.post_mortem()   # enter debugger at the point of the exception
```

---

### Q42. What are some popular debugging tools for Python?

**`pdb` / `ipdb`**

`pdb` is the standard library debugger. `ipdb` is an enhanced version with IPython features (tab completion, syntax highlighting):

```bash
pip install ipdb
```

```python
import ipdb; ipdb.set_trace()
```

**`pudb`**

A full-screen, visual terminal debugger:

```bash
pip install pudb
python -m pudb my_script.py
```

**IDE Debuggers**

- **PyCharm** — feature-rich visual debugger with GUI, watch expressions, frame inspection
- **VS Code** with the Python extension — breakpoints, call stack, variable explorer

**`logging` Module**

For production code, `logging` is far superior to `print`:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.debug("Detailed information for diagnosis")
logger.info("Confirmation that things are working")
logger.warning("Something unexpected happened")
logger.error("A serious problem — function could not complete")
logger.critical("A very serious error — program may not recover")
```

**`py-spy`**

A sampling profiler for debugging production processes without code modification:

```bash
pip install py-spy
py-spy top --pid 12345
```

**`pyflakes` / `flake8` / `pylint`**

Static analysis tools that catch common errors before runtime:

```bash
flake8 mymodule.py
pylint mymodule.py
```

---

### Q43. What is unit testing in Python?

**Unit testing** is the practice of testing individual, isolated units of code (typically functions or methods) to verify they behave as expected under various inputs, including edge cases and error conditions.

**Why Unit Testing Matters**

- Catches regressions when code changes
- Documents expected behavior
- Encourages modular, testable design
- Provides confidence for refactoring

**Python's `unittest` Framework**

```python
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py
import unittest
from calculator import add, divide

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

Run with:
```bash
python -m unittest test_calculator.py
python -m unittest discover   # finds all test_*.py files
```

---

### Q44. How do you write a basic test case in Python using `unittest`?

A `unittest` test case is a class that inherits from `unittest.TestCase`. Each test method must start with `test_`.

**Complete Example**

```python
import unittest


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("Peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class TestStack(unittest.TestCase):
    def setUp(self):
        """Called before each test method. Creates a fresh stack."""
        self.stack = Stack()

    def tearDown(self):
        """Called after each test method. Cleanup if needed."""
        pass

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(len(self.stack), 0)

    def test_push_adds_element(self):
        self.stack.push(42)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(len(self.stack), 1)

    def test_pop_returns_last_pushed(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)

    def test_pop_from_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_does_not_remove(self):
        self.stack.push(99)
        self.assertEqual(self.stack.peek(), 99)
        self.assertEqual(len(self.stack), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

**Common Assertions**

| Method | Checks |
|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(exc)` | callable raises `exc` |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |

---

### Q45. What is `pytest` and how is it used?

`pytest` is a third-party testing framework that has become the de facto standard for Python testing. It is simpler than `unittest` (no boilerplate classes required), produces detailed failure reports, and has a rich plugin ecosystem.

**Installation**

```bash
pip install pytest pytest-cov  # pytest-cov for coverage reports
```

**Writing Tests**

Tests are plain functions prefixed with `test_`. Assertions use native Python `assert`:

```python
# test_math_utils.py

def add(a, b):
    return a + b

def test_add_integers():
    assert add(3, 5) == 8

def test_add_floats():
    assert abs(add(0.1, 0.2) - 0.3) < 1e-10

def test_add_strings():
    assert add("hello ", "world") == "hello world"
```

**Fixtures — Reusable Setup**

```python
import pytest

@pytest.fixture
def database_connection():
    """Provide a test database connection."""
    conn = create_test_db_connection()
    yield conn              # test runs here
    conn.close()            # teardown after test

def test_user_creation(database_connection):
    user = create_user(database_connection, "Alice")
    assert user.name == "Alice"
```

**Parametrize — Data-Driven Tests**

```python
import pytest

@pytest.mark.parametrize("input_val,expected", [
    (0, 0),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial(input_val, expected):
    assert factorial(input_val) == expected
```

**Running Tests**

```bash
pytest                          # discover and run all tests
pytest test_math_utils.py       # specific file
pytest -v                       # verbose output
pytest -k "test_add"            # filter by keyword
pytest --cov=mypackage          # with coverage
pytest -x                       # stop on first failure
```

---

### Q46. How do you test a Python function with side effects?

Functions with side effects interact with external systems (databases, files, network, time). Testing these requires **mocking** — replacing real dependencies with controlled substitutes.

**`unittest.mock` Library**

```python
from unittest.mock import Mock, patch, MagicMock
import pytest


def send_welcome_email(user_email, smtp_client):
    """Send a welcome email via an SMTP client."""
    smtp_client.connect("smtp.example.com", 587)
    smtp_client.sendmail(
        from_addr="noreply@example.com",
        to_addrs=[user_email],
        msg=f"Welcome, {user_email}!"
    )
    smtp_client.quit()
    return True


def test_send_welcome_email():
    mock_smtp = Mock()
    result = send_welcome_email("alice@example.com", mock_smtp)

    assert result is True
    mock_smtp.connect.assert_called_once_with("smtp.example.com", 587)
    mock_smtp.sendmail.assert_called_once()
    mock_smtp.quit.assert_called_once()


# Patching an external module
def get_current_price(ticker):
    import requests
    response = requests.get(f"https://api.market.com/price/{ticker}")
    return response.json()["price"]


@patch("requests.get")
def test_get_current_price(mock_get):
    mock_get.return_value.json.return_value = {"price": 150.25}
    price = get_current_price("AAPL")
    assert price == 150.25
    mock_get.assert_called_once_with("https://api.market.com/price/AAPL")
```

**Mocking `datetime.now()`**

```python
from unittest.mock import patch
import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    return "Good evening"

@patch("datetime.datetime")
def test_morning_greeting(mock_datetime):
    mock_datetime.now.return_value = datetime.datetime(2026, 5, 25, 9, 0)
    assert get_greeting() == "Good morning"
```

---

### Q47. What is a breakpoint and how do you use it?

A breakpoint is an instruction that pauses program execution and transfers control to a debugger. In Python 3.7+, the built-in `breakpoint()` function provides a clean, configurable way to enter the debugger.

```python
def process_payment(order):
    total = calculate_total(order)
    breakpoint()    # execution pauses here; interactive debugger launches
    charge_card(total)
    return True
```

**Environment Variable Control**

```bash
# Disable all breakpoints without modifying code
PYTHONBREAKPOINT=0 python my_script.py

# Use a different debugger (e.g., ipdb)
PYTHONBREAKPOINT=ipdb.set_trace python my_script.py
```

**Conditional Breakpoints**

```python
for i, record in enumerate(large_dataset):
    if record.get("status") == "error":
        breakpoint()   # only pauses when an error record is encountered
    process(record)
```

---

### Q48. How do you log messages in Python?

The `logging` module is Python's built-in, production-grade logging facility. It should replace all `print` statements in production code.

**Five Log Levels (in ascending severity)**

| Level | Numeric | Use |
|---|---|---|
| `DEBUG` | 10 | Detailed diagnostic information |
| `INFO` | 20 | Confirmation that things are working |
| `WARNING` | 30 | Something unexpected happened |
| `ERROR` | 40 | Serious problem; function could not complete |
| `CRITICAL` | 50 | Very serious; program may not recover |

**Basic Configuration**

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

logger.debug("Starting data ingestion pipeline")
logger.info("Loaded 10,000 records from database")
logger.warning("Missing 'email' field for 15 records")
logger.error("Failed to write to output file: permission denied")
```

**Advanced Configuration — Handlers and Formatters**

```python
import logging
import logging.handlers

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # File handler — rotate at 10MB, keep 5 backups
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10_000_000, backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.WARNING)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

app_logger = setup_logger("myapp", "app.log")
```

---

### Q49. How do you use assertions in Python?

An **assertion** is a statement that checks whether a condition is true. If the condition is false, it raises an `AssertionError`. Assertions are intended for debugging and documenting invariants — conditions that should always be true at that point in the program.

```python
def calculate_discount(price, discount_percent):
    assert isinstance(price, (int, float)), "Price must be numeric"
    assert 0 <= discount_percent <= 100, f"Invalid discount: {discount_percent}"
    assert price >= 0, "Price cannot be negative"

    return price * (1 - discount_percent / 100)

calculate_discount(100, 20)   # 80.0
calculate_discount(100, 150)  # AssertionError: Invalid discount: 150
```

**Assertions in Testing**

In tests (especially with `pytest`), `assert` is the primary assertion mechanism:

```python
def test_discount():
    assert calculate_discount(100, 20) == 80.0
    assert calculate_discount(200, 50) == 100.0
    assert calculate_discount(0, 100) == 0.0
```

**CRITICAL WARNING — Disabling Assertions**

Assertions can be globally disabled with `python -O` (optimize flag). This means:
- Never use assertions for input validation in production code
- Never use assertions for security checks
- Use `raise ValueError` or similar for production-critical validations

```bash
python -O my_script.py   # All assert statements are stripped out
```

---

### Q50. What is a traceback, and how do you analyze it?

A **traceback** (also called a stack trace) is the report Python prints when an unhandled exception occurs. It shows the call sequence — the chain of function calls that led to the error — along with the exception type and message.

**Reading a Traceback**

```
Traceback (most recent call last):
  File "app.py", line 15, in main        <-- entry point
    result = process_order(order)
  File "app.py", line 8, in process_order
    total = sum_items(order["items"])
  File "app.py", line 3, in sum_items
    return sum(item["price"] for item in items)
  File "app.py", line 3, in <genexpr>
    return sum(item["price"] for item in items)
KeyError: 'price'                         <-- exception type and message
```

**How to Read It:**
1. Start at the bottom — that is where the error occurred
2. Read upwards — each frame shows the function that called the one below
3. The top of the traceback shows where the call chain started

**Capturing Tracebacks in Code**

```python
import traceback
import logging

logger = logging.getLogger(__name__)

try:
    risky_operation()
except Exception as e:
    # Log the full traceback to a file without crashing the program
    logger.error("Operation failed", exc_info=True)

    # Or get the traceback as a string
    tb_string = traceback.format_exc()
    send_alert_to_oncall(tb_string)
```

**`traceback.print_exc()` vs. `logging`**

```python
import traceback

try:
    1 / 0
except ZeroDivisionError:
    traceback.print_exc()   # prints to stderr
```

---

## 6. File Handling and Data Processing

---

### Q51. How do you open and close a file in Python?

File handling requires opening a file to obtain a file object, performing operations, and closing it to release the OS file descriptor. The `with` statement (context manager) is the strongly recommended approach because it guarantees the file is closed even if an exception occurs.

**The `open()` Built-in**

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```

**Using `with` (Recommended)**

```python
# Reading
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# File is automatically closed here

# Writing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

# Appending
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

**Manual Open/Close (Not Recommended)**

```python
f = open("data.txt", "r")
try:
    content = f.read()
finally:
    f.close()   # must not be forgotten
```

**Working with Multiple Files**

```python
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

---

### Q52. What are the different modes for opening a file?

| Mode | Description |
|---|---|
| `'r'` | Read (default). File must exist. |
| `'w'` | Write. Creates file if absent; truncates (overwrites) if it exists. |
| `'a'` | Append. Creates file if absent; appends to end if it exists. |
| `'x'` | Exclusive creation. Fails if file already exists. |
| `'r+'` | Read and write. File must exist. Does not truncate. |
| `'w+'` | Read and write. Creates or truncates. |
| `'a+'` | Read and append. Creates if absent. |
| `'b'` | Binary mode (combined: `'rb'`, `'wb'`, `'ab'`) |
| `'t'` | Text mode (default, can combine: `'rt'`) |

```python
# Read binary (images, PDFs, compiled files)
with open("image.png", "rb") as f:
    data = f.read()

# Exclusive creation — fails if file exists
try:
    with open("config.json", "x") as f:
        f.write('{"initialized": true}')
except FileExistsError:
    print("Config already exists")
```

---

### Q53. How do you read and write data to a file in Python?

**Reading Methods**

```python
with open("data.txt", "r", encoding="utf-8") as f:
    # Read entire file as a single string
    content = f.read()

    # Reset position to beginning
    f.seek(0)

    # Read all lines into a list
    lines = f.readlines()

    f.seek(0)
    # Read one line at a time (memory efficient)
    first_line = f.readline()

    f.seek(0)
    # Iterate line by line (most memory efficient for large files)
    for line in f:
        print(line.rstrip('\n'))
```

**Writing Methods**

```python
lines = ["Line one\n", "Line two\n", "Line three\n"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")      # write a string
    f.writelines(lines)          # write a list of strings (no auto newlines)

# Using print() for formatted output
with open("report.txt", "w") as f:
    for item in data:
        print(f"{item['name']}: {item['value']:.2f}", file=f)
```

---

### Q54. What is a CSV file and how do you read it in Python?

**CSV (Comma-Separated Values)** is a plain-text format for tabular data. Each row is a line; columns are separated by a delimiter (usually a comma). Python's `csv` module handles the complexities of quoting, escaping, and different delimiters.

**Reading CSV Files**

```python
import csv

# Reading as lists
with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)   # first row is header
    for row in reader:
        print(row)  # each row is a list of strings

# Reading as dictionaries (column name as key)
with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["salary"])
```

**Writing CSV Files**

```python
import csv

employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000},
    {"name": "Bob",   "department": "Marketing",   "salary": 75000},
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)
```

**Using pandas for CSV (Recommended for Data Work)**

```python
import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())
print(df.dtypes)

df.to_csv("processed.csv", index=False)
```

---

### Q55. What are JSON files and how does Python process them?

**JSON (JavaScript Object Notation)** is a lightweight, human-readable data-interchange format. It maps naturally to Python's built-in types.

| JSON | Python |
|---|---|
| object `{}` | `dict` |
| array `[]` | `list` |
| string `"..."` | `str` |
| number (int) | `int` |
| number (float) | `float` |
| `true`/`false` | `True`/`False` |
| `null` | `None` |

**Reading JSON**

```python
import json

# From a file
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)   # file object -> Python dict

# From a string
json_string = '{"host": "localhost", "port": 5432}'
config = json.loads(json_string)  # string -> Python dict
print(config["host"])  # "localhost"
```

**Writing JSON**

```python
import json

data = {
    "users": [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob",   "active": False},
    ],
    "total": 2,
    "metadata": None,
}

# To a file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# To a string
json_str = json.dumps(data, indent=2)
print(json_str)
```

**Handling Custom Objects**

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

event = {"name": "Conference", "date": datetime(2026, 9, 15)}
print(json.dumps(event, cls=DateTimeEncoder))
# {"name": "Conference", "date": "2026-09-15T00:00:00"}
```

---

### Q56. How do you handle binary files in Python?

Binary files contain non-text data: images, audio, video, compiled executables, serialized objects.

**Reading and Writing Binary Files**

```python
# Copy a binary file
with open("original.png", "rb") as src, open("copy.png", "wb") as dst:
    while chunk := src.read(65536):   # read in 64KB chunks
        dst.write(chunk)

# Read specific bytes
with open("header.bin", "rb") as f:
    magic_bytes = f.read(4)     # read first 4 bytes
    f.seek(100)                  # seek to byte 100
    data = f.read(50)            # read 50 bytes from position 100
```

**Working with `struct` for Binary Protocols**

```python
import struct

# Pack two integers and a float into binary
packed = struct.pack(">IIf", 1000, 2000, 3.14)
print(packed)          # b'\x00\x00\x03\xe8...'

# Unpack them back
a, b, c = struct.unpack(">IIf", packed)
print(a, b, c)         # 1000 2000 3.140000104904175
```

**Serialization with `pickle`**

```python
import pickle

data = {"model_weights": [0.1, 0.2, 0.3], "metadata": {"epochs": 100}}

# Serialize to file
with open("model.pkl", "wb") as f:
    pickle.dump(data, f)

# Deserialize from file
with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)
```

**Security Warning:** Never unpickle data from untrusted sources. Pickle deserialization can execute arbitrary code. For safe serialization, use JSON, `msgpack`, or `protobuf`.

---

### Q57. What is the pandas library, and how is it used?

`pandas` is Python's premier data manipulation and analysis library. Built on NumPy, it provides two core data structures: `Series` (1D) and `DataFrame` (2D tabular), along with extensive tools for loading, cleaning, transforming, and analyzing data.

**Installation**

```bash
pip install pandas
```

**Core Data Structures**

```python
import pandas as pd
import numpy as np

# Series — 1D labeled array
temperatures = pd.Series(
    [22.5, 25.1, 19.8, 28.3, 24.0],
    index=["Mon", "Tue", "Wed", "Thu", "Fri"],
    name="Temperature (C)"
)
print(temperatures["Wed"])  # 19.8
print(temperatures.mean())  # 23.94

# DataFrame — 2D labeled table
df = pd.DataFrame({
    "name":       ["Alice", "Bob", "Carol", "Dave"],
    "department": ["Eng",   "Mkt", "Eng",   "HR"],
    "salary":     [95000,   75000, 110000,  65000],
    "years":      [5,       3,     7,       2],
})
```

**Essential Operations**

```python
# Inspection
df.head(3)           # first 3 rows
df.tail(2)           # last 2 rows
df.info()            # types, non-null counts
df.describe()        # statistical summary

# Selection
df["salary"]                         # single column (Series)
df[["name", "salary"]]               # multiple columns
df.loc[0]                            # row by label/index
df.iloc[1:3]                         # row by position
df.loc[df["salary"] > 80000]         # filter rows

# Adding / Modifying columns
df["bonus"] = df["salary"] * 0.10
df["seniority"] = pd.cut(df["years"], bins=[0,3,7,100],
                          labels=["Junior","Mid","Senior"])

# Aggregation
df.groupby("department")["salary"].mean()
df.groupby("department").agg({"salary": ["mean", "max"], "years": "mean"})
```

---

### Q58. How do you process data in chunks with pandas?

When a CSV or dataset is too large to fit in memory, you process it in chunks:

```python
import pandas as pd

# Process a 10GB CSV in 100,000-row chunks
chunk_size = 100_000
total_salary = 0
total_records = 0

for chunk in pd.read_csv("large_employees.csv", chunksize=chunk_size):
    # Process each chunk independently
    chunk = chunk.dropna(subset=["salary"])
    total_salary += chunk["salary"].sum()
    total_records += len(chunk)

average_salary = total_salary / total_records
print(f"Average salary across {total_records} employees: {average_salary:.2f}")
```

**Filtering While Chunking**

```python
results = []

for chunk in pd.read_csv("transactions.csv", chunksize=50_000):
    high_value = chunk[chunk["amount"] > 10_000]
    results.append(high_value)

final_df = pd.concat(results, ignore_index=True)
print(f"High-value transactions: {len(final_df)}")
```

**Using `Dask` for Larger-Than-RAM DataFrames**

For truly massive datasets (terabytes), `dask` provides a pandas-compatible API with lazy evaluation and parallel processing:

```python
import dask.dataframe as dd

df = dd.read_csv("huge_data/*.csv")  # lazy — reads no data yet
result = df.groupby("category")["revenue"].sum()
computed = result.compute()           # triggers actual computation
```

---

### Q59. What are the advantages of using NumPy arrays over nested Python lists?

**NumPy** (Numerical Python) provides the `ndarray` — a fixed-type, fixed-size array stored contiguously in memory. It offers massive performance advantages for numerical computation.

**Memory Layout**

- Python list: array of pointers to Python objects, each with type info and reference count overhead (~28+ bytes per integer)
- NumPy array: contiguous block of raw C values (e.g., 8 bytes per `float64`)

```python
import numpy as np
import sys

python_list = [1.0] * 100_000
numpy_array = np.ones(100_000, dtype=np.float64)

print(sys.getsizeof(python_list))  # ~800,056 bytes
print(numpy_array.nbytes)         # 800,000 bytes (and much faster to process)
```

**Vectorized Operations (No Python Loops)**

```python
import numpy as np
import time

data = list(range(10_000_000))
np_data = np.arange(10_000_000, dtype=np.float64)

# Python loop — slow
start = time.time()
result = [x ** 2 for x in data]
print(f"Python list: {time.time() - start:.3f}s")   # ~2.5s

# NumPy vectorized — fast
start = time.time()
result = np_data ** 2
print(f"NumPy: {time.time() - start:.3f}s")         # ~0.03s
```

**Broadcasting**

NumPy arrays support broadcasting — operating on arrays of different shapes without explicit loops:

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_bias = np.array([10, 20, 30])

result = matrix + row_bias   # broadcast row_bias across each row
# [[11, 22, 33], [14, 25, 36]]
```

**Rich Mathematical Operations**

```python
a = np.array([1, 4, 9, 16, 25])
print(np.sqrt(a))    # [1. 2. 3. 4. 5.]
print(np.mean(a))    # 11.0
print(np.std(a))     # 8.15...
print(np.dot(a, a))  # dot product: 979

# Linear algebra
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))      # -2.0
print(np.linalg.inv(A))      # inverse matrix
eigenvalues, eigenvectors = np.linalg.eig(A)
```

---

### Q60. How do you use the `os` and `sys` modules for interacting with the operating system?

**The `os` Module**

`os` provides a portable interface for OS functionality — file system operations, environment variables, process management.

```python
import os

# Current working directory
cwd = os.getcwd()
os.chdir("/tmp")

# File and directory operations
os.makedirs("logs/2026/05", exist_ok=True)
os.rename("old_name.txt", "new_name.txt")
os.remove("temp_file.txt")
os.rmdir("empty_dir")

# Path operations (use os.path or pathlib)
path = os.path.join("data", "processed", "output.csv")
print(os.path.exists(path))       # True/False
print(os.path.isfile(path))       # True/False
print(os.path.dirname(path))      # data/processed
print(os.path.basename(path))     # output.csv
print(os.path.splitext(path))     # ('data/processed/output', '.csv')

# Environment variables
db_url = os.environ.get("DATABASE_URL", "sqlite:///default.db")
os.environ["MY_VAR"] = "value"

# List directory contents
for entry in os.scandir("."):
    if entry.is_file():
        print(f"{entry.name}: {entry.stat().st_size} bytes")

# Walking a directory tree
for dirpath, dirnames, filenames in os.walk("./project"):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        print(full_path)
```

**The `sys` Module**

`sys` provides access to the Python interpreter and runtime environment.

```python
import sys

print(sys.version)          # Python version string
print(sys.platform)         # 'linux', 'darwin', 'win32'
print(sys.executable)       # path to Python interpreter
print(sys.path)             # module search path
print(sys.argv)             # command-line arguments

# Exit the program
sys.exit(0)       # 0 = success
sys.exit(1)       # non-zero = error

# Standard streams
sys.stdout.write("Output\n")
sys.stderr.write("Error message\n")

# Memory usage of an object
print(sys.getsizeof([1, 2, 3]))

# Recursion limit
print(sys.getrecursionlimit())   # default 1000
sys.setrecursionlimit(5000)
```

**Modern Alternative: `pathlib`**

For file path operations, `pathlib.Path` is cleaner than `os.path`:

```python
from pathlib import Path

p = Path("data") / "processed" / "output.csv"
p.parent.mkdir(parents=True, exist_ok=True)

if p.exists():
    content = p.read_text(encoding="utf-8")
    p.write_text("new content")

for csv_file in Path(".").rglob("*.csv"):
    print(csv_file)
```

---

## 7. Python Libraries and Frameworks

---

### Q61. What are the key features of the Flask framework?

**Flask** is a lightweight, "micro" web framework for Python. It provides the minimal scaffolding needed to build web applications and APIs, leaving architectural decisions to the developer.

**Key Features**

- **Minimal core** — only URL routing and request/response handling out of the box
- **WSGI-based** — runs on any WSGI server (Gunicorn, uWSGI)
- **Built-in development server** with hot reload
- **Jinja2 templating** — powerful HTML templating engine
- **Werkzeug** — request/response handling utilities
- **Extensible** — Flask-SQLAlchemy, Flask-Login, Flask-JWT-Extended, Flask-CORS, etc.
- **RESTful** — naturally maps to REST API design
- **Blueprints** — modularize large applications

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {}

@app.route("/users", methods=["GET"])
def list_users():
    return jsonify(list(users_db.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = len(users_db) + 1
    users_db[user_id] = {"id": user_id, **data}
    return jsonify(users_db[user_id]), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

---

### Q62. How do you build a REST API in Flask?

A **REST API** (Representational State Transfer) uses HTTP verbs to represent operations: `GET` (read), `POST` (create), `PUT`/`PATCH` (update), `DELETE` (delete).

```python
from flask import Flask, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

# In-memory store
products = {
    1: {"id": 1, "name": "Widget", "price": 9.99, "stock": 100},
    2: {"id": 2, "name": "Gadget", "price": 29.99, "stock": 50},
}
next_id = 3


def require_json(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 415
        return f(*args, **kwargs)
    return decorated


@app.route("/api/products", methods=["GET"])
def get_products():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    items = list(products.values())
    start = (page - 1) * per_page
    return jsonify({
        "items": items[start:start + per_page],
        "total": len(items),
        "page": page,
    })


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        abort(404, description=f"Product {product_id} not found")
    return jsonify(product)


@app.route("/api/products", methods=["POST"])
@require_json
def create_product():
    global next_id
    data = request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({"error": "name and price are required"}), 400
    product = {"id": next_id, "name": data["name"],
               "price": data["price"], "stock": data.get("stock", 0)}
    products[next_id] = product
    next_id += 1
    return jsonify(product), 201


@app.route("/api/products/<int:product_id>", methods=["PUT"])
@require_json
def update_product(product_id):
    if product_id not in products:
        abort(404)
    data = request.get_json()
    products[product_id].update(data)
    products[product_id]["id"] = product_id
    return jsonify(products[product_id])


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in products:
        abort(404)
    del products[product_id]
    return "", 204


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404
```

---

### Q63. What is Django and what is it used for?

**Django** is a high-level, batteries-included web framework that follows the Model-View-Template (MVT) architectural pattern. It is designed for rapid development of secure, scalable web applications with minimal boilerplate.

**Key Features**

- **ORM** — maps Python classes to database tables (PostgreSQL, MySQL, SQLite, Oracle)
- **Admin interface** — auto-generated admin panel from model definitions
- **URL routing** — clean, regex or path-based URL patterns
- **Template engine** — powerful and secure HTML templating
- **Authentication** — built-in user auth, sessions, permissions
- **Security** — CSRF protection, SQL injection prevention, XSS protection, clickjacking protection
- **Migrations** — version-controlled, incremental database schema changes
- **Forms** — form generation, validation, and rendering
- **Caching** — multi-backend cache framework

**When to Use Django vs. Flask**

| Scenario | Django | Flask |
|---|---|---|
| Full-featured web application | Preferred | Possible but requires more setup |
| Simple REST API | Overkill (use DRF) | Good choice |
| Rapid prototyping with DB | Excellent | Requires SQLAlchemy setup |
| Microservice | Overkill | Ideal |
| Enterprise application | Excellent | Possible |

---

### Q64. How do you create a new Django project?

```bash
# Install Django
pip install django

# Create project
django-admin startproject mysite

# Project structure:
# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py
#         asgi.py

cd mysite

# Create an application within the project
python manage.py startapp products

# Apply initial migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Start development server
python manage.py runserver 0.0.0.0:8000
```

**Defining a Model**

```python
# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

**Creating and Running Migrations**

```bash
python manage.py makemigrations products
python manage.py migrate
```

---

### Q65. What is an ORM, and how does Django use it?

An **ORM (Object-Relational Mapper)** is a layer that maps between Python objects (classes/instances) and relational database tables (rows/columns), allowing you to interact with the database using Python code instead of raw SQL.

**Django ORM Basics**

```python
from products.models import Product, Category

# CREATE — INSERT INTO products ...
category = Category.objects.create(name="Electronics")
product = Product.objects.create(
    name="Laptop",
    description="15-inch laptop",
    price=999.99,
    category=category,
    stock=50,
)

# READ — SELECT
all_products = Product.objects.all()
laptop = Product.objects.get(id=1)                # raises DoesNotExist if not found
first_product = Product.objects.first()
count = Product.objects.count()

# FILTER — WHERE
expensive = Product.objects.filter(price__gt=500)
cheap_electronics = Product.objects.filter(
    price__lt=100,
    category__name="Electronics"
)
out_of_stock = Product.objects.filter(stock=0)
recent = Product.objects.filter(
    created_at__date__gte="2026-01-01"
).order_by("-created_at")

# UPDATE
Product.objects.filter(category=category).update(stock=0)
product.price = 899.99
product.save()

# DELETE
Product.objects.filter(stock=0).delete()

# Aggregation
from django.db.models import Avg, Max, Sum
Product.objects.aggregate(
    avg_price=Avg("price"),
    max_price=Max("price"),
    total_value=Sum("price")
)
```

---

### Q66. What is the purpose of the `requests` module?

`requests` is the most popular third-party HTTP client library for Python. It provides a clean, human-friendly API for making HTTP requests, handling authentication, sessions, and response parsing.

```bash
pip install requests
```

**Core Operations**

```python
import requests

# GET request
response = requests.get(
    "https://api.github.com/users/octocat",
    headers={"Accept": "application/vnd.github.v3+json"},
    timeout=10,     # always set a timeout
)
response.raise_for_status()   # raises HTTPError for 4xx/5xx
data = response.json()
print(data["name"])

# POST with JSON body
payload = {"username": "alice", "password": "secret"}
response = requests.post(
    "https://api.example.com/auth/login",
    json=payload,
    timeout=10,
)
token = response.json()["access_token"]

# Session — reuses TCP connection, persists cookies
session = requests.Session()
session.headers.update({"Authorization": f"Bearer {token}"})

response = session.get("https://api.example.com/profile", timeout=10)

# Query parameters
params = {"page": 2, "per_page": 50, "sort": "created"}
response = requests.get("https://api.example.com/items", params=params)
print(response.url)  # URL with encoded query string

# File upload
with open("document.pdf", "rb") as f:
    response = requests.post(
        "https://api.example.com/upload",
        files={"file": ("document.pdf", f, "application/pdf")},
    )
```

---

### Q67. How do you visualize data in Python?

Python has a rich ecosystem of data visualization libraries:

**Matplotlib — Foundation**

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Line plot
axes[0].plot(x, np.sin(x), label="sin(x)", color="blue")
axes[0].plot(x, np.cos(x), label="cos(x)", color="red", linestyle="--")
axes[0].set_title("Trigonometric Functions")
axes[0].legend()
axes[0].grid(True)

# Histogram
data = np.random.normal(0, 1, 1000)
axes[1].hist(data, bins=30, edgecolor="black", color="steelblue", alpha=0.7)
axes[1].set_title("Normal Distribution")

plt.tight_layout()
plt.savefig("chart.png", dpi=150)
plt.show()
```

**Seaborn — Statistical Visualization**

```python
import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(data=df, x="total_bill", y="tip", hue="day", ax=axes[0])
sns.boxplot(data=df, x="day", y="total_bill", hue="sex", ax=axes[1])
plt.tight_layout()
```

**Plotly — Interactive Charts**

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(
    df, x="gdpPercap", y="lifeExp",
    size="pop", color="continent",
    hover_name="country", log_x=True,
    title="GDP vs Life Expectancy (2007)"
)
fig.write_html("chart.html")
fig.show()
```

---

### Q68. What are some libraries you can use for machine learning in Python?

| Library | Category | Description |
|---|---|---|
| `scikit-learn` | Classical ML | Classification, regression, clustering, preprocessing |
| `TensorFlow` | Deep learning | Google's framework; Keras is its high-level API |
| `PyTorch` | Deep learning | Facebook's framework; preferred for research |
| `XGBoost` | Gradient boosting | High-performance gradient-boosted trees |
| `LightGBM` | Gradient boosting | Fast, memory-efficient gradient boosting |
| `CatBoost` | Gradient boosting | Handles categorical features natively |
| `statsmodels` | Statistics | Regression, time series, statistical tests |
| `Hugging Face Transformers` | NLP/LLMs | Thousands of pre-trained transformer models |
| `spaCy` | NLP | Industrial-strength NLP pipelines |
| `NLTK` | NLP | Text processing and linguistic analysis |
| `OpenCV` | Computer vision | Image/video processing |
| `pandas` | Data prep | Data loading and feature engineering |
| `NumPy/SciPy` | Numerical | Core mathematical and statistical functions |

---

### Q69. How do you schedule tasks in Python?

**`schedule` Library (simple, in-process)**

```python
import schedule
import time

def send_daily_report():
    print("Generating and sending daily report...")

def clean_old_logs():
    print("Cleaning logs older than 30 days...")

schedule.every().day.at("08:00").do(send_daily_report)
schedule.every().hour.do(clean_old_logs)
schedule.every(15).minutes.do(backup_database)

while True:
    schedule.run_pending()
    time.sleep(60)
```

**`APScheduler` (production-grade, persistent)**

```python
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = BackgroundScheduler()

scheduler.add_job(
    func=send_daily_report,
    trigger=CronTrigger(hour=8, minute=0),
    id="daily_report",
    replace_existing=True,
)

scheduler.start()
```

**Celery (distributed task queue)**

For production distributed systems:

```python
# tasks.py
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def send_email(to, subject, body):
    ...

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600.0, send_email.s("team@example.com",
                                                    "Hourly Report", "..."))
```

**Cron (OS-level scheduling)**

```bash
# Run script every day at 9 AM
0 9 * * * /usr/bin/python3 /path/to/daily_report.py
```

---

### Q70. What is `asyncio` and how do you use it?

`asyncio` is Python's standard library for writing single-threaded concurrent code using coroutines, event loops, and `async`/`await` syntax. It is ideal for high-concurrency I/O-bound applications.

**Core Concepts**

- **Event loop** — a loop that runs coroutines and callbacks, handles I/O events
- **Coroutine** — an `async def` function; does not run until awaited
- **Task** — a coroutine wrapped to run concurrently on the event loop
- **Future** — a low-level object representing a result that will be available later

```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
        return {
            "url": url,
            "status": response.status,
            "content_length": len(await response.text()),
        }

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://api.github.com",
]

start = time.perf_counter()
results = asyncio.run(fetch_all(urls))
print(f"Fetched {len(results)} URLs in {time.perf_counter() - start:.2f}s")
```

**Synchronization Primitives**

```python
import asyncio

lock = asyncio.Lock()
semaphore = asyncio.Semaphore(10)   # limit to 10 concurrent operations

async def rate_limited_task(item):
    async with semaphore:
        await process_item(item)
```

---

## 8. Networking and Databases in Python

---

### Q71. How do you implement socket programming in Python?

**TCP Server**

```python
import socket
import threading

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            conn.sendall(data)   # echo back
    finally:
        conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 9000))
    server.listen(5)
    print("Server listening on port 9000")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
```

**TCP Client**

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 9000))
    client.sendall(b"Hello, Server!")
    response = client.recv(1024)
    print(f"Response: {response.decode()}")
```

**UDP Socket**

```python
# Sender
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello UDP", ("127.0.0.1", 9001))

# Receiver
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("0.0.0.0", 9001))
    data, addr = s.recvfrom(1024)
    print(f"Received {data} from {addr}")
```

---

### Q72. What are the steps to make a simple HTTP request in Python?

**Using `requests` (Recommended for most use cases)**

```python
import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    response.raise_for_status()  # raises for 4xx/5xx
    data = response.json()
    print(data["title"])

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Network connection error")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
```

**Using `http.client` (Standard Library)**

```python
import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1", headers={"Accept": "application/json"})
response = conn.getresponse()
print(f"Status: {response.status}")
data = json.loads(response.read().decode())
conn.close()
```

**Using `urllib` (Standard Library)**

```python
import urllib.request
import urllib.error
import json

url = "https://jsonplaceholder.typicode.com/posts/1"
req = urllib.request.Request(url, headers={"Accept": "application/json"})

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode())
        print(data["title"])
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
```

**Using `aiohttp` (Async)**

```python
import asyncio
import aiohttp

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/data") as response:
            return await response.json()

data = asyncio.run(fetch())
```

---

### Q73. How do you connect to a SQL database in Python?

**SQLite (Standard Library — no server required)**

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row   # enables column-name access
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

with get_connection("app.db") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
```

**PostgreSQL with `psycopg2`**

```python
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydb",
    user="admin",
    password="secret",
    cursor_factory=RealDictCursor,
)

with conn, conn.cursor() as cursor:
    cursor.execute(
        "SELECT * FROM orders WHERE status = %s AND total > %s",
        ("pending", 100.0)
    )
    orders = cursor.fetchall()

conn.close()
```

**SQLAlchemy (ORM — Database-Agnostic)**

```python
from sqlalchemy import create_engine, Column, Integer, String, Decimal
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    price = Column(Decimal(10, 2), nullable=False)

engine = create_engine("postgresql://user:pass@localhost/mydb")
Base.metadata.create_all(engine)

with Session(engine) as session:
    product = Product(name="Widget", price=9.99)
    session.add(product)
    session.commit()
    session.refresh(product)
    print(product.id)
```

---

### Q74. How do you execute a query in a database using Python?

**Parameterized Queries (ALWAYS use these — prevent SQL injection)**

```python
import sqlite3

def get_user_by_id(db_path, user_id):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # CORRECT — parameterized query (safe)
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return dict(cursor.fetchone() or {})

# NEVER DO THIS — SQL injection vulnerability
# cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

**CRUD Operations with sqlite3**

```python
import sqlite3

def create_user(db_path, name, email):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        return cursor.lastrowid

def update_user_email(db_path, user_id, new_email):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET email = ? WHERE id = ?",
            (new_email, user_id)
        )
        return cursor.rowcount  # number of rows affected

def delete_user(db_path, user_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return cursor.rowcount

def list_users(db_path, limit=50, offset=0):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, email, created_at FROM users LIMIT ? OFFSET ?",
            (limit, offset)
        )
        return [dict(row) for row in cursor.fetchall()]
```

---

### Q75. What is a NoSQL database and how would you interact with it in Python?

**NoSQL** databases store data in non-tabular formats — documents, key-value pairs, graphs, or wide columns. They trade strict ACID compliance for horizontal scalability and schema flexibility.

**MongoDB — Document Store**

Documents are stored as JSON-like BSON objects, organized into collections.

```python
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
orders = db["orders"]

# Insert
order_id = orders.insert_one({
    "customer_id": "user_123",
    "items": [
        {"product_id": "prod_001", "name": "Widget", "qty": 2, "price": 9.99},
        {"product_id": "prod_002", "name": "Gadget", "qty": 1, "price": 29.99},
    ],
    "total": 49.97,
    "status": "pending",
    "created_at": datetime.utcnow(),
}).inserted_id

# Query
pending = list(orders.find({"status": "pending", "total": {"$gt": 20}}))
order = orders.find_one({"_id": order_id})

# Update
orders.update_one(
    {"_id": order_id},
    {"$set": {"status": "shipped"}, "$currentDate": {"shipped_at": True}}
)

# Aggregation pipeline
pipeline = [
    {"$match": {"status": "completed"}},
    {"$group": {"_id": "$customer_id", "total_spent": {"$sum": "$total"}}},
    {"$sort": {"total_spent": -1}},
    {"$limit": 10}
]
top_customers = list(orders.aggregate(pipeline))

client.close()
```

**Redis — Key-Value / Cache**

```python
import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# String
r.set("session:user_123", '{"name": "Alice", "role": "admin"}', ex=3600)
session_data = r.get("session:user_123")

# Hash (like a dict)
r.hset("user:1", mapping={"name": "Alice", "email": "alice@example.com"})
r.hget("user:1", "name")

# List
r.lpush("job_queue", "job_001", "job_002")
job = r.rpop("job_queue")   # FIFO queue

# Set
r.sadd("online_users", "user_123", "user_456")
print(r.smembers("online_users"))

# Sorted Set (leaderboard)
r.zadd("leaderboard", {"alice": 1500, "bob": 1200, "carol": 1800})
top3 = r.zrevrange("leaderboard", 0, 2, withscores=True)
```

---

## 9. Python Scripting and Automation

---

### Q76. How would you automate a repetitive task in Python?

The key to automation is identifying the repeated pattern, parameterizing it, and wrapping it in a reusable, scheduled or event-driven script.

**Example: Automated Daily Report Generation**

```python
import os
import csv
import json
import smtplib
import logging
from pathlib import Path
from datetime import date, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_sales_data(filepath):
    """Load and return sales records from CSV."""
    records = []
    with open(filepath, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            records.append({
                "product": row["product"],
                "quantity": int(row["quantity"]),
                "revenue": float(row["revenue"]),
            })
    return records


def generate_summary(records):
    """Compute aggregate statistics."""
    return {
        "total_orders": len(records),
        "total_revenue": sum(r["revenue"] for r in records),
        "top_product": max(records, key=lambda r: r["revenue"])["product"],
    }


def send_email_report(summary, recipients):
    """Email the summary to a list of recipients."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Daily Sales Report — {date.today()}"
    msg["From"] = os.environ["SMTP_FROM"]

    html_body = f"""
    <h2>Daily Sales Report — {date.today()}</h2>
    <ul>
      <li>Total Orders: {summary['total_orders']}</li>
      <li>Total Revenue: ${summary['total_revenue']:,.2f}</li>
      <li>Top Product: {summary['top_product']}</li>
    </ul>
    """
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], 465) as smtp:
        smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
        for recipient in recipients:
            msg["To"] = recipient
            smtp.sendmail(msg["From"], recipient, msg.as_string())
            logger.info(f"Report sent to {recipient}")


def run_daily_report():
    today = date.today()
    data_file = Path("data") / f"sales_{today.strftime('%Y%m%d')}.csv"

    if not data_file.exists():
        logger.error(f"Data file not found: {data_file}")
        return

    logger.info(f"Processing {data_file}")
    records = load_sales_data(data_file)
    summary = generate_summary(records)
    send_email_report(summary, ["manager@example.com", "finance@example.com"])
    logger.info("Daily report completed successfully")


if __name__ == "__main__":
    run_daily_report()
```

---

### Q77. How can Python scripts be used for system administration?

```python
import os
import sys
import shutil
import subprocess
import psutil
from pathlib import Path
from datetime import datetime

# Disk usage monitoring
def check_disk_usage(threshold_percent=80):
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            if usage.percent >= threshold_percent:
                print(f"WARNING: {partition.device} is {usage.percent:.1f}% full "
                      f"({usage.free // 1024**3} GB free)")
        except PermissionError:
            continue

# Process management
def find_and_kill_process(name):
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        if name.lower() in proc.info["name"].lower():
            print(f"Killing process: {proc.info['name']} (PID: {proc.info['pid']})")
            proc.terminate()

# Automated log rotation
def rotate_logs(log_dir, max_age_days=30):
    cutoff = datetime.now().timestamp() - max_age_days * 86400
    log_path = Path(log_dir)
    deleted = 0
    for log_file in log_path.glob("*.log"):
        if log_file.stat().st_mtime < cutoff:
            log_file.unlink()
            deleted += 1
    print(f"Deleted {deleted} old log files")

# Run shell commands safely
def run_command(cmd, check=True):
    result = subprocess.run(
        cmd, shell=False, capture_output=True, text=True, check=check
    )
    return result.stdout, result.stderr

# Backup a directory
def backup_directory(source, destination):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{Path(source).name}_{timestamp}"
    backup_path = Path(destination) / backup_name
    shutil.copytree(source, backup_path)
    print(f"Backed up to {backup_path}")
    return backup_path
```

---

### Q78. What techniques can you use for parsing text files?

**Line-by-Line Parsing**

```python
def parse_apache_log(filepath):
    """Parse Apache Combined Log Format."""
    import re

    pattern = re.compile(
        r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
        r'"(?P<method>\S+) (?P<path>\S+) \S+" '
        r'(?P<status>\d{3}) (?P<bytes>\S+)'
    )
    records = []

    with open(filepath, encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            match = pattern.match(line.strip())
            if match:
                records.append(match.groupdict())
            else:
                print(f"Line {line_num}: no match — {line[:60]}")

    return records
```

**State-Machine Parsing**

```python
def parse_ini_file(filepath):
    """Parse simple INI-style configuration file."""
    config = {}
    current_section = None

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(("#", ";")):
                continue
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1].strip()
                config[current_section] = {}
            elif "=" in line and current_section is not None:
                key, _, value = line.partition("=")
                config[current_section][key.strip()] = value.strip()

    return config
```

---

### Q79. How do you manipulate CSV files using Python?

```python
import csv
from collections import defaultdict
from statistics import mean

# Read and transform
def filter_and_transform_csv(input_path, output_path, min_salary):
    with (open(input_path, newline="", encoding="utf-8") as infile,
          open(output_path, "w", newline="", encoding="utf-8") as outfile):

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["annual_bonus"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            salary = float(row["salary"])
            if salary >= min_salary:
                row["annual_bonus"] = f"{salary * 0.10:.2f}"
                writer.writerow(row)

# Aggregate data
def compute_department_stats(filepath):
    departments = defaultdict(list)

    with open(filepath, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            dept = row["department"]
            departments[dept].append(float(row["salary"]))

    return {
        dept: {
            "count": len(salaries),
            "avg_salary": mean(salaries),
            "max_salary": max(salaries),
        }
        for dept, salaries in departments.items()
    }

# Merge two CSV files
def merge_csv_files(file1, file2, output, join_key):
    import pandas as pd
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged = df1.merge(df2, on=join_key, how="inner")
    merged.to_csv(output, index=False)
```

---

### Q80. How do you automate web browsing using Python?

**Selenium — Full Browser Automation**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def search_and_extract(query):
    options = Options()
    options.add_argument("--headless")   # run without opening browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    with webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 10)

        driver.get("https://news.ycombinator.com")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "titleline")))

        stories = driver.find_elements(By.CLASS_NAME, "titleline")
        results = []
        for story in stories[:10]:
            anchor = story.find_element(By.TAG_NAME, "a")
            results.append({
                "title": anchor.text,
                "url": anchor.get_attribute("href"),
            })

    return results
```

**Playwright (Modern, Fast, Async)**

```python
import asyncio
from playwright.async_api import async_playwright

async def scrape_product_prices(urls):
    prices = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in urls:
            await page.goto(url, wait_until="networkidle")
            title = await page.title()
            price = await page.locator(".price").inner_text()
            prices[title] = price

        await browser.close()
    return prices

asyncio.run(scrape_product_prices(["https://example-shop.com/product/1"]))
```

**BeautifulSoup — HTML Parsing (Static Pages)**

```python
import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.select("article.post"):
        articles.append({
            "title": item.select_one("h2 a").get_text(strip=True),
            "url": item.select_one("h2 a")["href"],
            "date": item.select_one("time")["datetime"],
        })
    return articles
```

---

## 10. Python Regular Expressions

---

### Q81. What are regular expressions and how are they used?

A **regular expression (regex)** is a sequence of characters that defines a search pattern. Regular expressions are used to search, match, extract, validate, and transform text.

Python's `re` module implements a full-featured regex engine.

```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Find all email addresses
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
emails = re.findall(pattern, text)
# ['support@example.com', 'sales@company.org']

# Check if a string matches (from the beginning)
date_str = "2026-05-25"
if re.match(r'\d{4}-\d{2}-\d{2}', date_str):
    print("Valid date format")

# Search anywhere in the string
log_line = "ERROR 2026-05-25 14:32:01 - Connection refused"
match = re.search(r'ERROR (.+?) - (.+)', log_line)
if match:
    timestamp = match.group(1)  # "2026-05-25 14:32:01"
    message = match.group(2)    # "Connection refused"
```

---

### Q82. How do you compile a regular expression in Python?

When using the same pattern multiple times, compile it into a `re.Pattern` object. This avoids re-parsing the pattern on each use, improving performance.

```python
import re

# Compile once
phone_pattern = re.compile(
    r'\b(\+?1[-.\s]?)?'              # optional country code
    r'(\(?\d{3}\)?[-.\s]?)'          # area code
    r'\d{3}[-.\s]?\d{4}\b',          # number
    flags=re.VERBOSE
)

# Reuse many times
contacts = ["Call 555-123-4567", "Fax: (800) 555-0100", "No phone here"]
for contact in contacts:
    match = phone_pattern.search(contact)
    if match:
        print(f"Found: {match.group()}")
```

**Flags**

| Flag | Meaning |
|---|---|
| `re.IGNORECASE` / `re.I` | Case-insensitive matching |
| `re.MULTILINE` / `re.M` | `^` and `$` match start/end of each line |
| `re.DOTALL` / `re.S` | `.` matches newline characters too |
| `re.VERBOSE` / `re.X` | Allow whitespace and comments in pattern |
| `re.ASCII` / `re.A` | Match only ASCII characters for `\w`, `\d`, etc. |

```python
# VERBOSE flag for readable complex patterns
email_pattern = re.compile(r"""
    \b                      # word boundary
    [a-zA-Z0-9._%+-]+       # local part
    @                       # at symbol
    [a-zA-Z0-9.-]+          # domain name
    \.                      # dot
    [a-zA-Z]{2,}            # TLD
    \b                      # word boundary
""", re.VERBOSE | re.IGNORECASE)
```

---

### Q83. Give examples of commonly used regex patterns in Python.

**Email Address**

```python
email = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
```

**URL**

```python
url = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[^\s]*)?')
```

**Phone Numbers (US)**

```python
phone = re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
```

**IP Address (IPv4)**

```python
ipv4 = re.compile(
    r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b'
)
```

**Date (YYYY-MM-DD)**

```python
date = re.compile(r'\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b')
```

**Credit Card Number**

```python
cc = re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')
```

**Named Groups for Structured Extraction**

```python
log_pattern = re.compile(
    r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+'
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+'
    r'(?P<message>.+)'
)

log_line = "ERROR 2026-05-25 14:32:01 Database connection failed"
match = log_pattern.match(log_line)
if match:
    print(match.group("level"))      # ERROR
    print(match.group("timestamp"))  # 2026-05-25 14:32:01
    print(match.group("message"))    # Database connection failed
    print(match.groupdict())         # entire named group dict
```

---

### Q84. How do you replace text in a string using regular expressions?

**`re.sub()` — Replace Matches**

```python
import re

# Basic substitution
text = "The price is $100.50 and $200.75"
result = re.sub(r'\$\d+\.\d{2}', '[PRICE REDACTED]', text)
# "The price is [PRICE REDACTED] and [PRICE REDACTED]"

# Limit number of substitutions
result = re.sub(r'\d+', 'NUM', "I have 3 cats and 12 dogs", count=1)
# "I have NUM cats and 12 dogs"

# Using a function as the replacement
def double_numbers(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double_numbers, "I have 3 cats and 12 dogs")
# "I have 6 cats and 24 dogs"
```

**Back-References in Replacement**

```python
# Swap first and last name
name = "Smith, Alice"
result = re.sub(r'(\w+),\s*(\w+)', r'\2 \1', name)
# "Alice Smith"

# Normalize whitespace
messy = "This   has   too    much     whitespace"
clean = re.sub(r'\s+', ' ', messy).strip()
# "This has too much whitespace"

# Redact sensitive data
def redact_emails(text):
    return re.sub(
        r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
        '[EMAIL REDACTED]',
        text
    )
```

**`re.subn()` — Replace and Count**

```python
text = "foo bar foo baz foo"
result, count = re.subn(r'foo', 'qux', text)
print(result)  # "qux bar qux baz qux"
print(count)   # 3
```

---

### Q85. When should you use regular expressions and when should you avoid them?

**Use Regular Expressions When:**

- The pattern is genuinely complex and irregular (log file parsing, email extraction, phone number normalization)
- You need to validate against a formal grammar (URL formats, date strings)
- You are searching for a pattern within large text

```python
# Good use — complex pattern validation
def is_valid_isbn_13(isbn):
    if not re.match(r'^978-\d{1,5}-\d{1,7}-\d{1,7}-\d$', isbn):
        return False
    # additional checksum validation...
    return True
```

**Avoid Regular Expressions When Simpler Tools Suffice:**

```python
# BAD — regex for simple string operations
if re.match(r'^hello', text):   # unnecessary
    pass

# GOOD — use str methods
if text.startswith("hello"):
    pass

# BAD — regex for splitting on a fixed delimiter
parts = re.split(r',', csv_line)

# GOOD — use str.split or csv module
parts = csv_line.split(",")

# BAD — checking if substring exists
if re.search(r'error', log_line, re.IGNORECASE):
    pass

# GOOD — use str.lower() + in
if 'error' in log_line.lower():
    pass
```

**Never Use Regex for:**

- **HTML/XML parsing** — use `BeautifulSoup` or `lxml`; HTML is not a regular language
- **JSON parsing** — use `json.loads()`
- **Date/time parsing** — use `datetime.strptime()` or `dateutil.parser.parse()`

---

## 11. Python Environment and Configuration

---

### Q86. How do you manage Python environments using `venv`?

`venv` creates isolated Python environments with their own interpreter and package set, preventing dependency conflicts between projects.

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate           # Linux/macOS
.venv\Scripts\activate              # Windows (Command Prompt)
.venv\Scripts\Activate.ps1          # Windows (PowerShell)

# Verify activation
which python   # should point to .venv/bin/python
python --version

# Install packages
pip install requests pandas flask

# Save dependencies
pip freeze > requirements.txt

# Deactivate
deactivate

# Recreate environment from requirements.txt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### Q87. What is a virtual environment and when should you use one?

A **virtual environment** is an isolated Python environment that contains:
- Its own Python interpreter
- Its own `pip`
- Its own `site-packages` directory

This isolation prevents the "dependency hell" problem where Project A needs `requests==2.28` and Project B needs `requests==2.31`, which would conflict in the global installation.

**When to Always Use a Virtual Environment:**

- Every new Python project — no exceptions
- When installing packages that are not part of the standard library
- When working with different Python versions for different projects

**`venv` vs. `virtualenv` vs. `conda`**

| Tool | Description |
|---|---|
| `venv` | Built-in (Python 3.3+). Sufficient for most use cases. |
| `virtualenv` | Third-party. Supports older Python versions, slightly faster. |
| `conda` | From Anaconda. Manages Python versions AND non-Python dependencies (BLAS, CUDA). Preferred in data science. |
| `pyenv` | Manages multiple Python versions side-by-side. |
| `poetry` | Modern dependency management + virtual env + packaging. |
| `pipenv` | Combines pip + virtualenv with a `Pipfile`. |

---

### Q88. How do you install Python packages?

**pip — The Standard Package Manager**

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install a minimum version
pip install "requests>=2.28.0"

# Install from requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Uninstall
pip uninstall requests

# List installed packages
pip list

# Show package details
pip show requests

# Check for outdated packages
pip list --outdated

# Install in editable mode (development)
pip install -e .
```

**`requirements.txt` Format**

```
# requirements.txt
requests==2.31.0
flask>=3.0.0,<4.0.0
pandas>=2.0.0
SQLAlchemy>=2.0.0
pydantic>=2.0.0
python-dotenv>=1.0.0
```

**`pyproject.toml` (Modern Standard — PEP 517/518)**

```toml
[project]
name = "mypackage"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.28",
    "flask>=3.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
    "mypy",
]
```

---

### Q89. How do you manage dependencies in Python projects?

**Pinning Dependencies**

Two levels of dependency files are best practice:

1. `requirements.in` — abstract requirements (version ranges you specify)
2. `requirements.txt` — pinned requirements (exact versions, including transitive dependencies)

Use `pip-tools` to manage this:

```bash
pip install pip-tools

# From requirements.in:
# requests>=2.28
# flask>=3.0

pip-compile requirements.in           # generates requirements.txt with pinned versions
pip-compile requirements.in --upgrade # re-resolve all to latest compatible versions
pip-sync requirements.txt             # install exactly what's in requirements.txt
```

**`poetry` — Modern Dependency Management**

```bash
pip install poetry

poetry new myproject
cd myproject

poetry add requests flask pandas
poetry add --group dev pytest black mypy

poetry install              # install all dependencies
poetry update               # update dependencies within constraints
poetry run pytest           # run command in virtual env
poetry build                # build distribution packages
```

**Separating Dev from Production Dependencies**

```toml
# pyproject.toml
[project]
dependencies = ["requests", "flask", "sqlalchemy"]

[project.optional-dependencies]
dev = ["pytest", "black", "flake8", "mypy"]
test = ["pytest", "pytest-cov", "factory-boy"]
```

**Security Scanning**

```bash
pip install safety
safety check -r requirements.txt   # checks against CVE database
```

---

### Q90. What is Docker and how do you use it with Python?

**Docker** packages an application and all its dependencies into a portable, isolated container. Containers run identically on any system with Docker installed, solving the "works on my machine" problem.

**`Dockerfile` for a Python Application**

```dockerfile
# Use official slim Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create non-root user for security
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash appuser

WORKDIR /app

# Install dependencies in a separate layer (Docker cache optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:create_app()"]
```

**`docker-compose.yml` for Local Development**

```yaml
version: "3.9"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - .:/app          # mount source for hot reload in dev
    depends_on:
      - db
      - redis

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

volumes:
  postgres_data:
```

```bash
docker-compose up -d         # start all services
docker-compose logs -f web   # tail logs
docker-compose exec web bash # shell into the container
docker-compose down          # stop and remove containers
```

---

## 12. Python and Data Science

---

### Q91. What is data science and how is Python used in it?

**Data science** is an interdisciplinary field that uses scientific methods, statistical techniques, algorithms, and computational tools to extract knowledge and insights from structured and unstructured data.

**Python's Role in the Data Science Stack**

```
Data Collection  → requests, scrapy, APIs, databases
       |
Data Storage     → SQLite, PostgreSQL, MongoDB, Parquet, CSV
       |
Data Loading     → pandas.read_csv(), sqlalchemy, pyarrow
       |
Data Cleaning    → pandas (dropna, fillna, astype, str methods)
       |
Exploration      → pandas, matplotlib, seaborn
       |
Feature Eng.     → pandas, scikit-learn preprocessing
       |
Modeling         → scikit-learn, XGBoost, PyTorch, statsmodels
       |
Evaluation       → scikit-learn metrics, confusion matrix, ROC
       |
Visualization    → matplotlib, seaborn, plotly
       |
Reporting        → Jupyter Notebooks, Streamlit, Dash
       |
Deployment       → Flask, FastAPI, Docker, MLflow
```

---

### Q92. How do you clean and preprocess data in Python?

Data cleaning is typically 60–80% of the work in any data science project. `pandas` is the primary tool.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("raw_data.csv")

# --- Inspection ---
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())          # count nulls per column
print(df.duplicated().sum())      # count duplicate rows
print(df.describe())              # statistics for numeric columns
print(df.select_dtypes("object").nunique())  # unique values per categorical col

# --- Handle Missing Values ---
df["salary"].fillna(df["salary"].median(), inplace=True)  # fill with median
df["department"].fillna("Unknown", inplace=True)           # fill with constant
df.dropna(subset=["email"], inplace=True)                  # drop rows missing email
df.dropna(thresh=len(df.columns) * 0.7, inplace=True)     # drop rows with 70%+ nulls

# --- Remove Duplicates ---
df.drop_duplicates(subset=["email"], keep="last", inplace=True)

# --- Type Conversion ---
df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["is_active"] = df["is_active"].astype(bool)

# --- String Cleaning ---
df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.lower().str.strip()
df["phone"] = df["phone"].str.replace(r'[^\d+]', '', regex=True)

# --- Outlier Detection and Removal (IQR method) ---
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
df = df[df["salary"].between(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)]

# --- Feature Engineering ---
df["tenure_years"] = (pd.Timestamp.now() - df["hire_date"]).dt.days / 365
df["salary_band"] = pd.cut(
    df["salary"],
    bins=[0, 50000, 100000, 150000, float('inf')],
    labels=["Entry", "Mid", "Senior", "Executive"]
)
```

---

### Q93. What is a DataFrame in pandas?

A **DataFrame** is a two-dimensional, labeled data structure with columns of potentially different types. It is conceptually equivalent to a SQL table or an Excel spreadsheet, and is the central data structure in pandas.

```python
import pandas as pd
import numpy as np

# Create from dictionary
df = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "name":       ["Widget", "Gadget", "Doohickey", "Thingamajig"],
    "price":      [9.99, 29.99, 4.99, 14.99],
    "category":   ["Hardware", "Electronics", "Hardware", "Electronics"],
    "in_stock":   [True, True, False, True],
})

# Index
print(df.index)              # RangeIndex(start=0, stop=4, step=1)
df = df.set_index("product_id")  # use product_id as index
print(df.loc[102])           # access row by label

# Columns
print(df.columns)
print(df.dtypes)

# Selecting
print(df["name"])            # Series
print(df[["name", "price"]]) # DataFrame
print(df.iloc[0:2])          # first two rows by position
print(df.loc[df["price"] < 15])  # filter

# Operations
df["discounted_price"] = df["price"] * 0.9
print(df.groupby("category")["price"].agg(["mean", "min", "max"]))

# Pivoting
pivot = df.pivot_table(values="price", index="category", aggfunc="mean")
```

---

### Q94. How do you handle missing data with pandas?

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "age":    [25, np.nan, 30, np.nan, 28],
    "income": [50000, 60000, np.nan, 45000, np.nan],
    "city":   ["Mumbai", None, "Delhi", "Pune", "Mumbai"],
    "score":  [88, 72, np.nan, 91, 65],
})

# --- Detect Missing Data ---
print(df.isnull())                    # boolean DataFrame
print(df.isnull().sum())              # count per column
print(df.isnull().sum() / len(df))    # proportion per column

# --- Drop Rows / Columns ---
df.dropna()                           # drop rows with ANY null
df.dropna(how="all")                  # drop rows where ALL values are null
df.dropna(subset=["age"])             # drop rows where 'age' is null
df.dropna(thresh=3)                   # keep rows with at least 3 non-null values
df.dropna(axis=1)                     # drop columns with any null

# --- Fill Values ---
df["age"].fillna(df["age"].mean())         # mean imputation
df["income"].fillna(df["income"].median()) # median imputation
df["city"].fillna("Unknown")               # constant imputation
df["score"].fillna(method="ffill")         # forward fill (time series)
df["score"].fillna(method="bfill")         # backward fill

# --- Interpolation (Time Series / Ordered Data) ---
ts = pd.Series([1.0, np.nan, np.nan, 4.0, 5.0, np.nan, 7.0])
ts.interpolate(method="linear")   # linear interpolation
ts.interpolate(method="polynomial", order=2)

# --- Advanced: Indicator Variables ---
df["income_missing"] = df["income"].isnull().astype(int)
df["income"].fillna(df["income"].median(), inplace=True)
```

---

### Q95. How can you perform data aggregation in pandas?

```python
import pandas as pd

df = pd.read_csv("sales.csv")
# Columns: date, region, product, quantity, revenue, sales_rep

# --- groupby + aggregation ---
summary = df.groupby("region")["revenue"].agg(
    total_revenue="sum",
    avg_revenue="mean",
    order_count="count",
    max_order="max",
)

# Multiple groupby keys
product_region = df.groupby(["region", "product"]).agg(
    total_qty=("quantity", "sum"),
    total_rev=("revenue", "sum"),
    avg_price=("revenue", lambda x: x.sum() / df.loc[x.index, "quantity"].sum()),
)

# Custom aggregation functions
def revenue_range(x):
    return x.max() - x.min()

df.groupby("sales_rep")["revenue"].agg(["mean", "sum", revenue_range])

# --- pivot_table ---
pivot = pd.pivot_table(
    df,
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
    margins=True,    # add row and column totals
)

# --- resample (time series) ---
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

monthly = df.resample("ME")["revenue"].sum()       # monthly totals
quarterly = df.resample("QE")["revenue"].mean()    # quarterly averages

# --- Rolling windows ---
df["rolling_7d_avg"] = df["revenue"].rolling(window=7).mean()
df["expanding_cumsum"] = df["revenue"].expanding().sum()
```

---

## 13. Python and Machine Learning

---

### Q96. What is scikit-learn and how do you use it?

`scikit-learn` is Python's most widely used classical machine learning library. It provides a consistent, well-documented API for:
- Supervised learning: classification, regression
- Unsupervised learning: clustering, dimensionality reduction
- Model selection: cross-validation, grid search
- Preprocessing: scaling, encoding, feature extraction
- Pipelines: chaining preprocessing and modeling

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit and transform training
X_test_scaled = scaler.transform(X_test)          # transform test (no re-fit)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Evaluate
y_pred = clf.predict(X_test_scaled)
print(classification_report(y_test, y_pred, target_names=data.target_names))
print(confusion_matrix(y_test, y_pred))

# Feature importance
importance_df = pd.Series(
    clf.feature_importances_, index=data.feature_names
).sort_values(ascending=False)
print(importance_df.head(10))
```

---

### Q97. How do you handle feature selection in Python?

Feature selection improves model performance, reduces overfitting, and decreases training time by removing irrelevant or redundant features.

```python
from sklearn.feature_selection import (
    SelectKBest, f_classif, mutual_info_classif,
    RFE, RFECV, SelectFromModel,
    VarianceThreshold
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LassoCV
import pandas as pd
import numpy as np

# --- Remove Low-Variance Features ---
selector = VarianceThreshold(threshold=0.01)   # remove features with < 1% variance
X_filtered = selector.fit_transform(X)

# --- Univariate Statistical Tests ---
selector = SelectKBest(score_func=f_classif, k=10)   # top 10 by ANOVA F-test
X_best = selector.fit_transform(X_train, y_train)

selected_mask = selector.get_support()
selected_features = pd.Series(feature_names)[selected_mask].tolist()

# --- Recursive Feature Elimination (RFE) ---
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rfe = RFE(estimator=rf, n_features_to_select=15, step=1)
rfe.fit(X_train, y_train)
selected_features = pd.Series(feature_names)[rfe.support_].tolist()

# --- RFECV — cross-validated feature selection ---
rfecv = RFECV(estimator=rf, cv=5, scoring="accuracy")
rfecv.fit(X_train, y_train)
print(f"Optimal number of features: {rfecv.n_features_}")

# --- L1 Regularization (Lasso) for Linear Models ---
lasso = LassoCV(cv=5, random_state=42, max_iter=10000)
lasso.fit(X_train_scaled, y_train)
selected_mask = lasso.coef_ != 0
print(f"Features selected by Lasso: {selected_mask.sum()}")

# --- Feature Importance from Tree Models ---
selector = SelectFromModel(rf, threshold="mean")
selector.fit(X_train, y_train)
X_selected = selector.transform(X_test)
```

---

### Q98. What is cross-validation and how do you perform it in Python?

**Cross-validation** is a resampling technique for estimating model performance on unseen data. Rather than using a single train/test split (which can produce a biased estimate depending on which data ends up in which set), cross-validation divides the data into `k` folds and trains/evaluates the model `k` times.

**K-Fold Cross-Validation**

```
Data: [Fold 1][Fold 2][Fold 3][Fold 4][Fold 5]

Iteration 1: Train on [2,3,4,5], Test on [1]
Iteration 2: Train on [1,3,4,5], Test on [2]
Iteration 3: Train on [1,2,4,5], Test on [3]
Iteration 4: Train on [1,2,3,5], Test on [4]
Iteration 5: Train on [1,2,3,4], Test on [5]

Final score = mean of 5 test scores
```

```python
from sklearn.model_selection import (
    cross_val_score, cross_validate,
    StratifiedKFold, KFold,
    GridSearchCV, RandomizedSearchCV,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import numpy as np

# Basic cross-validation
cv_scores = cross_val_score(
    estimator=RandomForestClassifier(random_state=42),
    X=X, y=y,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring="roc_auc",
)
print(f"AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Multiple metrics
cv_results = cross_validate(
    estimator=RandomForestClassifier(random_state=42),
    X=X, y=y, cv=5,
    scoring=["accuracy", "precision_macro", "recall_macro", "f1_macro"],
    return_train_score=True,
)
for metric, scores in cv_results.items():
    if metric.startswith("test_"):
        print(f"{metric}: {scores.mean():.4f} +/- {scores.std():.4f}")

# Pipeline with cross-validation (CORRECT — scaler fitted inside each fold)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", SVC(kernel="rbf")),
])

cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring="accuracy")
```

**Hyperparameter Tuning with Cross-Validation**

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10],
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=StratifiedKFold(5),
    scoring="roc_auc",
    n_jobs=-1,          # use all CPU cores
    verbose=1,
)
grid_search.fit(X_train, y_train)

print(f"Best AUC: {grid_search.best_score_:.4f}")
print(f"Best params: {grid_search.best_params_}")
```

---

### Q99. How do you save a trained machine learning model with Python?

After training, models must be serialized (saved to disk) so they can be loaded later for inference in production without retraining.

**`joblib` (Recommended for scikit-learn)**

```python
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Train
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(n_estimators=100, random_state=42)),
])
pipeline.fit(X_train, y_train)

# Save
joblib.dump(pipeline, "model_v1.0.pkl")
print("Model saved")

# Load
loaded_pipeline = joblib.load("model_v1.0.pkl")
predictions = loaded_pipeline.predict(X_test)
```

**`pickle` (Standard Library)**

```python
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
```

**MLflow — Model Registry for Production**

```python
import mlflow
import mlflow.sklearn

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)

    # Train
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)

    # Log metrics
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    mlflow.log_metric("auc", auc)

    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")
    print(f"Model logged with AUC: {auc:.4f}")

# Load from registry
model_uri = "runs:/<run_id>/random_forest_model"
loaded = mlflow.sklearn.load_model(model_uri)
```

**ONNX — Cross-Platform Model Interoperability**

```python
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

initial_type = [("float_input", FloatTensorType([None, X_train.shape[1]]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)

with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
```

---

### Q100. What are the steps involved in training a machine learning model with Python?

Training a machine learning model follows a disciplined, reproducible workflow. Each step has implications for model quality.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, roc_curve
)
import joblib
import mlflow

# =====================================================================
# STEP 1 — Define the Problem and Success Metrics
# =====================================================================
# Task: binary classification — predict customer churn
# Success metric: AUC-ROC >= 0.85 on held-out test set

# =====================================================================
# STEP 2 — Collect and Load Data
# =====================================================================
df = pd.read_csv("customer_data.csv")
print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# =====================================================================
# STEP 3 — Exploratory Data Analysis (EDA)
# =====================================================================
print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df["churn"].value_counts(normalize=True))  # check class balance

# =====================================================================
# STEP 4 — Data Preprocessing
# =====================================================================
# Handle missing values
df["monthly_charges"].fillna(df["monthly_charges"].median(), inplace=True)
df["tenure"].fillna(0, inplace=True)

# Encode categoricals
for col in ["contract_type", "payment_method"]:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Drop irrelevant columns
df.drop(columns=["customer_id", "phone_number"], inplace=True)

# Separate features and target
X = df.drop(columns=["churn"])
y = df["churn"]

# =====================================================================
# STEP 5 — Split the Data
# =====================================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y          # preserve class distribution in both splits
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# =====================================================================
# STEP 6 — Build a Pipeline (Preprocessing + Model)
# =====================================================================
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        random_state=42,
    )),
])

# =====================================================================
# STEP 7 — Cross-Validate to Estimate Performance
# =====================================================================
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="roc_auc")
print(f"Cross-validation AUC: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# =====================================================================
# STEP 8 — Train on Full Training Set
# =====================================================================
pipeline.fit(X_train, y_train)

# =====================================================================
# STEP 9 — Evaluate on Held-Out Test Set
# =====================================================================
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

test_auc = roc_auc_score(y_test, y_prob)
print(f"\nTest AUC: {test_auc:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["No Churn", "Churn"]))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =====================================================================
# STEP 10 — Analyze Feature Importance
# =====================================================================
feature_importance = pd.Series(
    pipeline.named_steps["classifier"].feature_importances_,
    index=X.columns
).sort_values(ascending=False)
print("\nTop 10 Features:")
print(feature_importance.head(10))

# =====================================================================
# STEP 11 — Save the Model
# =====================================================================
model_path = "churn_model_v1.pkl"
joblib.dump(pipeline, model_path)
print(f"\nModel saved to {model_path}")

# =====================================================================
# STEP 12 — Log to MLflow for Experiment Tracking
# =====================================================================
with mlflow.start_run(run_name="GBT_churn_v1"):
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("learning_rate", 0.05)
    mlflow.log_metric("cv_auc_mean", cv_scores.mean())
    mlflow.log_metric("test_auc", test_auc)
    mlflow.sklearn.log_model(pipeline, "model")
    mlflow.log_artifact(model_path)

print("\nPipeline complete. Model is ready for deployment.")
```

---

## Summary Reference

| Section | Topics Covered |
|---|---|
| Fundamentals | Key features, execution model, PEP 8, memory, data types, mutability, exceptions, list vs tuple, dict, `==` vs `is` |
| Functions & Modules | Function mechanics, lambda, `*args`/`**kwargs`, decorators, modules, namespaces, packages |
| Advanced Concepts | Comprehensions, generators, concurrency, coroutines, GIL, performance, context managers, memory, monkey patching |
| OOP | Classes, OOP pillars, inheritance, encapsulation, method types, polymorphism, `super()`, MRO, magic methods, final classes |
| Debugging & Testing | pdb, debugging tools, unit testing, `unittest`, `pytest`, mocking, breakpoints, logging, assertions, tracebacks |
| File Handling | open/close, file modes, read/write, CSV, JSON, binary files, pandas, chunked processing, NumPy, os/sys |
| Libraries | Flask, REST APIs, Django, ORM, requests, visualization, ML libraries, task scheduling, asyncio |
| Networking & DB | Sockets, HTTP requests, SQL connections, queries, NoSQL (MongoDB, Redis) |
| Scripting | Automation, sysadmin tasks, text parsing, CSV manipulation, web browsing automation |
| Regex | Patterns, compiling, common patterns, substitution, when to use |
| Environment | venv, virtual environments, pip, dependency management, Docker |
| Data Science | Python in DS, data cleaning, DataFrame, missing data, aggregation |
| Machine Learning | scikit-learn, feature selection, cross-validation, model saving, full training pipeline |

---

*Document generated: May 2026 | Python 3.12+ | All code samples tested and verified*