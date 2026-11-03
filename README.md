# Class XI Informatics Practices (065) - Practical File

Practical record file of **Aditya Shakya**, Class XI - A, Section A, Roll No. 2,
Ridhima World School. Session 2026 - 2027.

Submitted to **Mr. Arya Sir**, Department of Computer Science.

The printable practical file is in this repository:

**[IP_Practical_File_Class_11_Aditya_Shakya.pdf](IP_Practical_File_Class_11_Aditya_Shakya.pdf)** - 10 pages, A4, ready to print.

## Contents

Seventeen Python programs and six SQL commands, as prescribed for the session.

| No. | Practical | File |
|-----|-----------|------|
| 1 | Interactive Mode Execution | [python/01_interactive_mode.txt](python/01_interactive_mode.txt) |
| 2 | Script Mode Execution | [python/02_script_mode.py](python/02_script_mode.py) |
| 3 | Python Keywords and Identifiers | [python/03_keywords_and_identifiers.py](python/03_keywords_and_identifiers.py) |
| 4 | Dynamic Typing and Variable Assignment | [python/04_dynamic_typing.py](python/04_dynamic_typing.py) |
| 5 | Standard Data Types | [python/05_data_types.py](python/05_data_types.py) |
| 6 | Input and Output Statements | [python/06_input_and_output.py](python/06_input_and_output.py) |
| 7 | Explicit Type Conversion (Typecasting) | [python/07_type_conversion.py](python/07_type_conversion.py) |
| 8 | Arithmetic Operators | [python/08_arithmetic_operators.py](python/08_arithmetic_operators.py) |
| 9 | Relational and Logical Operators | [python/09_relational_logical_operators.py](python/09_relational_logical_operators.py) |
| 10 | Conditional Constructs (if, if-else) | [python/10_if_else.py](python/10_if_else.py) |
| 11 | Multi-way Conditional Branching (if-elif-else) | [python/11_if_elif_else.py](python/11_if_elif_else.py) |
| 12 | The range() Function | [python/12_range_function.py](python/12_range_function.py) |
| 13 | Iteration with for Loop | [python/13_for_loop.py](python/13_for_loop.py) |
| 14 | Iteration with while Loop | [python/14_while_loop.py](python/14_while_loop.py) |
| 15 | String Operations and Index Slicing | [python/15_string_operations.py](python/15_string_operations.py) |
| 16 | Lists Manipulation | [python/16_lists.py](python/16_lists.py) |
| 17 | Dictionaries (Key-Value Mapping) | [python/17_dictionaries.py](python/17_dictionaries.py) |
| 18 | CREATE TABLE - Creating a Table | [sql/18_create_table.sql](sql/18_create_table.sql) |
| 19 | DROP TABLE - Deleting a Table | [sql/19_drop_table.sql](sql/19_drop_table.sql) |
| 20 | INSERT INTO - Adding Records | [sql/20_insert_into.sql](sql/20_insert_into.sql) |
| 21 | UPDATE - Modifying Records | [sql/21_update.sql](sql/21_update.sql) |
| 22 | DELETE - Removing Records | [sql/22_delete.sql](sql/22_delete.sql) |
| 23 | SELECT - Retrieving Data | [sql/23_select.sql](sql/23_select.sql) |

## Running the programs

Every Python program runs on Python 3 with the standard library only:

```bash
python3 python/08_arithmetic_operators.py
```

Practical 1 is a transcript of the interactive interpreter session, so it is kept
as a `.txt` file - type those lines at the `>>>` prompt rather than running the file.

The SQL practicals are written for MySQL 8. They are meant to be run in order,
from Practical 18 to Practical 23, because they work on the same `student` table
in the database `school`:

```bash
mysql -u root -p < sql/18_create_table.sql
```

## Outputs

The output of every program and query, along with a short conclusion, is recorded
in the PDF above. The outputs shown there were produced by actually running each
program, and the SQL results were verified against a live database.
