<div align="center">

# Informatics Practices (065)

### Class XI Practical File &nbsp;·&nbsp; 17 Python Programs &nbsp;·&nbsp; 6 SQL Commands

[![Python](https://img.shields.io/badge/Python-3.12-3776AB
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1
[![Practicals](https://img.shields.io/badge/Practicals-23-1F3864
[![Pages](https://img.shields.io/badge/PDF-10_pages-C0392B

**Aditya Shakya** &nbsp;·&nbsp; Class XI - A &nbsp;·&nbsp; Roll No. 2
**Ridhima World School** &nbsp;·&nbsp; Session 2026 - 2027
*Submitted to **Mr. Arya Sir**, Department of Computer Science*

[**Open the practical file (PDF)**](IP_Practical_File_Class_11_Aditya_Shakya.pdf) &nbsp;|&nbsp; [Python](#part-a--python-programming) &nbsp;|&nbsp; [SQL](#part-b--sql) &nbsp;|&nbsp; [All outputs](PRACTICALS.md)

</div>

---

## Why this repository

This is the complete practical record for **Informatics Practices (Code 065), Class XI** -
the same file that is printed and submitted, kept here so every program is one click away
and can actually be run.

- Every program was **executed**, so the outputs in the PDF are real results, not typed by hand.
- The six SQL practicals work on **one `student` table**, run in order from 18 to 23.
- The printable file is **10 pages on A4**, designed to print cleanly in black and white.

|  |  |  |
|:--:|:--:|:--:|
| **23**<br/>Practicals | **17**<br/>Python programs | **6**<br/>SQL commands |

---

## Contents

### Part A · Python Programming

| No. | Practical | Source |
|:---:|-----------|:------:|
| | **Unit 1 · Introduction to Python & Basics** | |
| `01` | Interactive Mode Execution | [`01_interactive_mode.txt`](python/01_interactive_mode.txt) |
| `02` | Script Mode Execution | [`02_script_mode.py`](python/02_script_mode.py) |
| `03` | Python Keywords and Identifiers | [`03_keywords_and_identifiers.py`](python/03_keywords_and_identifiers.py) |
| `04` | Dynamic Typing and Variable Assignment | [`04_dynamic_typing.py`](python/04_dynamic_typing.py) |
| | **Unit 2 · Data Handling & Operators** | |
| `05` | Standard Data Types | [`05_data_types.py`](python/05_data_types.py) |
| `06` | Input and Output Statements | [`06_input_and_output.py`](python/06_input_and_output.py) |
| `07` | Explicit Type Conversion (Typecasting) | [`07_type_conversion.py`](python/07_type_conversion.py) |
| `08` | Arithmetic Operators | [`08_arithmetic_operators.py`](python/08_arithmetic_operators.py) |
| `09` | Relational and Logical Operators | [`09_relational_logical_operators.py`](python/09_relational_logical_operators.py) |
| | **Unit 3 · Flow Control & Loops** | |
| `10` | Conditional Constructs (if, if-else) | [`10_if_else.py`](python/10_if_else.py) |
| `11` | Multi-way Conditional Branching (if-elif-else) | [`11_if_elif_else.py`](python/11_if_elif_else.py) |
| `12` | The range() Function | [`12_range_function.py`](python/12_range_function.py) |
| `13` | Iteration with for Loop | [`13_for_loop.py`](python/13_for_loop.py) |
| `14` | Iteration with while Loop | [`14_while_loop.py`](python/14_while_loop.py) |
| | **Unit 4 · Data Structures** | |
| `15` | String Operations and Index Slicing | [`15_string_operations.py`](python/15_string_operations.py) |
| `16` | Lists Manipulation | [`16_lists.py`](python/16_lists.py) |
| `17` | Dictionaries (Key-Value Mapping) | [`17_dictionaries.py`](python/17_dictionaries.py) |

### Part B · SQL

| No. | Practical | Type | Source |
|:---:|-----------|:----:|:------:|
| `18` | CREATE TABLE - Creating a Table | `DDL` | [`18_create_table.sql`](sql/18_create_table.sql) |
| `19` | DROP TABLE - Deleting a Table | `DDL` | [`19_drop_table.sql`](sql/19_drop_table.sql) |
| `20` | INSERT INTO - Adding Records | `DML` | [`20_insert_into.sql`](sql/20_insert_into.sql) |
| `21` | UPDATE - Modifying Records | `DML` | [`21_update.sql`](sql/21_update.sql) |
| `22` | DELETE - Removing Records | `DML` | [`22_delete.sql`](sql/22_delete.sql) |
| `23` | SELECT - Retrieving Data | `DQL` | [`23_select.sql`](sql/23_select.sql) |

---

## Quick start

```bash
git clone https://github.com/zionixxdev/xi-ip-practicals.git
cd xi-ip-practicals

# run any Python practical
python3 python/08_arithmetic_operators.py

# run the SQL practicals in order (MySQL 8)
mysql -u root -p < sql/18_create_table.sql
mysql -u root -p < sql/20_insert_into.sql
mysql -u root -p < sql/23_select.sql
```

Practical 1 is a transcript of the interactive interpreter, so it lives in
`python/01_interactive_mode.txt` - type those lines at the `>>>` prompt instead of running the file.
A few programs read input from the keyboard; enter the values when prompted.

---

## Repository layout

```
xi-ip-practicals/
├── IP_Practical_File_Class_11_Aditya_Shakya.pdf   the printable 10-page file
├── PRACTICALS.md                                  every program with its output
├── python/
│   ├── 01_interactive_mode.txt
│   ├── 02_script_mode.py
│   ├── ...
│   └── 17_dictionaries.py
└── sql/
    ├── 18_create_table.sql
    ├── ...
    └── 23_select.sql
```

---

## Outputs

[**PRACTICALS.md**](PRACTICALS.md) lists all 23 practicals with the aim, the full code and the
output it produced. The same material, laid out for printing with a cover, certificate, index
and conclusions, is in the [PDF](IP_Practical_File_Class_11_Aditya_Shakya.pdf).

---

<div align="center">

**Made for the session 2026 - 2027**

[![GitHub](https://img.shields.io/badge/github-zionixxdev-181717

</div>
