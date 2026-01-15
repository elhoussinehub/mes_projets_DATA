# Welcome to My Ds Babel
***

## Task
The goal of this project is to create a lightweight data-conversion tool that transforms CSV files into SQLite tables and vice-versa, without relying on any external libraries. The challenge is to clean messy CSV headers, generate valid SQL schemas dynamically, and ensure that the insertion of data works correctly even with inconsistent formatting.

## Description
This project solves the data-processing problem by implementing two core functions:

1. sql_to_csv(database, table_name)

Reads an SQLite table and converts it into a clean CSV-formatted string. Column names are extracted, rows are retrieved, and the entire output is returned as plain text.

2. csv_to_sql(csv_content, database, table_name)

Takes a CSV file (or StringIO object), sanitizes its headers by removing invalid characters, automatically creates the SQL table, and inserts every row safely using SQLite parameterized queries.

The system ensures:

Automatic cleaning of column names

Handling numeric column names

Safe SQL (no string concatenation for row data)

Full compatibility with the Python standard library

Ability to process any CSV into a ready-to-use SQLite database

This tool is ideal for learning SQL basics, Python I/O operations, and data cleaning techniques

## Installation
Since this project uses only Python’s built-in modules (csv and sqlite3), there is nothing to install.
Simply clone the repository:

git clone https://github.com/yourusername/my_ds_babel.git
cd my_ds_babel

## Usage
Run the script from the terminal, passing a CSV input and output database name.
```
python my_ds_babel.py input.csv output.db
./my_project argument1 argument2
```
