# Data-Science-Learning-Journey
My daily progress in Data Science
# 🧠 Python Concepts – From Lists to OOP

This repository contains my Python learning journey where I covered core concepts from basic *Lists* to *Object-Oriented Programming (OOP)* including *Classes* and *Objects*.

---

## 📘 Covered Topics

This single notebook includes:

1. ✅ Lists – Creating, indexing, slicing, methods  
2. ✅ Tuples – Immutable data structures  
3. ✅ Sets – Unique value collections  
4. ✅ Dictionaries – Key-value pairs  
5. ✅ Loops – for, while, nested loops  
6. ✅ Conditional Statements – if, elif, else  
7. ✅ Functions – Definition, arguments, return values  
8. ✅ Object-Oriented Programming (OOP)  
   - Classes & Objects  
   - __init__ constructor  
   - Instance variables  
   - Methods  

---

## 🚀 Next Steps

I'll be moving forward with:

- Inheritance & Polymorphism in OOP  
- Exception Handling  
- Numpy, Pandas  
- Data Visualization  
- Machine Learning Algorithms  
- Projects

# 📊 NumPy and Pandas Practice

Welcome to my repository for practicing and mastering **NumPy** and **Pandas** — the foundational libraries for data analysis and scientific computing in Python.

---

## 📌 Contents

- 🧮 NumPy Basics
- 🐼 Pandas Fundamentals
- 📊 Data Cleaning & Analysis
- 📈 Aggregation & Grouping
- 🔄 Data Merging, Joining, Concatenation
- 📉 Time Series & Visualization (Optional)

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure Python 3.7+ is installed. Use `pip` to install required packages:

```bash
pip install numpy pandas
# 🐼 Data Manipulation using Pandas

This repository contains hands-on practice and examples of **data manipulation techniques using Pandas**, a powerful Python library for data analysis. The focus is on real-world tasks like cleaning, transforming, and analyzing structured data effectively.

---

## 📌 Key Topics Covered

- 🔹 Series & DataFrames
- 🔹 Reading and Writing Data (CSV, Excel, JSON)
- 🔹 Indexing, Selecting, and Filtering
- 🔹 Handling Missing Data
- 🔹 Data Transformation
- 🔹 Merging, Joining, and Concatenating
- 🔹 GroupBy and Aggregation
- 🔹 Sorting and Ranking
- 🔹 Pivot Tables & Crosstabs
- 🔹 Working with Dates and Time Series

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure you have Python 3.7+ installed and install Pandas:

```bash
pip install pandas
# 🗄️ SQLite Database Project

This project uses an SQLite database file to store and manage data locally without the need for a dedicated database server.

## 📁 Project Contents

- `your_file.db` – The main SQLite database file.
- `main.py` or `app.py` – Script to interact with the database (insert, query, update, delete).
- `README.md` – Project documentation.

## 🐍 How to Use

### 1. Prerequisites

Ensure Python is installed. SQLite comes bundled with Python as part of the `sqlite3` module.

### 2. Interact with the Database

You can use a script like this to access the database:

```python
import sqlite3

conn = sqlite3.connect('your_file.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

conn.close()

🚦 Understanding Python GIL with a Real-World Analogy
🧠 What is GIL (Global Interpreter Lock)?
The Global Interpreter Lock (GIL) is a mutex used by CPython (the standard Python implementation) to ensure that only one thread executes Python bytecode at a time, even on multi-core processors.

🛣️ GIL = Single-Lane Bridge Analogy
Imagine you're managing delivery trucks (threads) trying to cross a single-lane bridge (the GIL). No matter how many trucks (threads) you have or how many drivers (CPU cores) are available, only one truck can cross at a time.

arduino
Copy
Edit
🚚 Truck 1 → |==== Bridge ====| → ✅
🚚 Truck 2 → [waiting]
🚚 Truck 3 → [waiting]
Threading in Python (with GIL) = All trucks wait their turn.

CPU cores are mostly idle, waiting for their truck's turn to cross.

🔁 When is Threading Still Useful?
Let’s say trucks are just carrying paperwork (I/O-bound tasks like file I/O, API requests):

While one truck is at a toll booth (waiting for data), another can jump on the bridge.

✅ Threading is good here because threads spend more time waiting than computing.

🧱 When Threading Fails: Heavy Lifting (CPU-Bound)
Now imagine the trucks are loaded with bricks (CPU-heavy tasks like math, image processing).

Each truck takes time and effort to cross.

🚫 Only one CPU core is used effectively due to the GIL.

Threading doesn’t speed things up — it just adds overhead.

✅ Solution: Multiprocessing = Multiple Bridges!
Instead of one lane, what if you build multiple bridges?

That's what multiprocessing does — it creates separate processes, each with its own Python interpreter and memory space. Now each truck can cross its own bridge at the same time using different CPU cores.

arduino
Copy
Edit
🚚 Truck 1 → |==== Bridge 1 ====| → ✅ (Core 1)
🚚 Truck 2 → |==== Bridge 2 ====| → ✅ (Core 2)
🚚 Truck 3 → |==== Bridge 3 ====| → ✅ (Core 3)
📌 Summary Table
Scenario	Use Threading	Use Multiprocessing
I/O-bound tasks	✅ Yes	✅ Optional
CPU-bound tasks	❌ No	✅ Yes
Shared memory	✅ Easy	❌ Harder (requires Queue/Manager)
True parallelism	❌ No (GIL)	✅ Yes

🔧 That’s Why This Project Uses multiprocessing
In this project, we rely on multiprocessing for tasks like:

Parallel data processing

Heavy computation

Image transformations

Model training

This ensures the app runs faster by utilizing all available CPU cores, bypassing the GIL limitation.



