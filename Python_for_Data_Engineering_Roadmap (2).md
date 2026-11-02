# Python for Data Engineering — Complete Roadmap & Progress Tracker

Purpose: A complete topic map to track Python skills needed for practical, job-ready Data Engineering work.

Progress key:
- COMPLETED — covered in lessons
- IN PROGRESS — started or needs revision
- NOT STARTED — pending

Priority key:
- [CORE] — most useful in day-to-day Data Engineering work and interviews
- [IMPORTANT] — strongly recommended for production-ready Python
- [ADDITIONAL] — useful after the core skills are comfortable

This roadmap focuses on Python and Python-based data handling. Keep ADF, CDC, incremental loading, dbt, Spark/PySpark, and other separate Data Engineering technologies for later, after completing this Python roadmap.

---

## Phase 1 — Python Foundations for Data Engineering

Status: COMPLETED (logging needs strengthening)

- Python syntax and execution flow
- Variables, data types, type conversion
- Operators and expressions
- Conditions: if, elif, else
- Loops: for and while
- Functions, parameters, return values, scope
- Strings and common string operations
- Lists, tuples, sets, dictionaries
- List and dictionary methods
- List/dictionary comprehensions
- Iteration: range, enumerate, zip
- Working with files and folders
- [CORE] File handling: open, read, readline, readlines, write, append
- [CORE] File pointers: tell and seek
- [CORE] Context managers: with open(...)
- [CORE] CSV file reading and writing
- [CORE] JSON reading and writing
- Exception handling: try, except, else, finally, raise
- [IMPORTANT] Logging: levels, formatting, timestamps, writing logs to files, exception tracebacks
- Basic debugging and reading error messages

## Phase 2 — Python Project Structure, Modules and Environments

Status: NOT STARTED

- [CORE] Modules and imports
- Built-in modules: os, pathlib, sys, csv, json, datetime, re, math, collections
- [CORE] Creating and importing custom Python modules
- Packages and package structure
- __init__.py and package imports
- Absolute and relative imports
- [CORE] Virtual environments
- Installing and managing packages with pip
- requirements.txt and dependency versions
- Understanding Python interpreter and package paths
- Running Python files from the terminal
- Project folder structure
- Reusable utility/helper modules
- [IMPORTANT] Git-friendly project organization
- Avoiding circular imports

## Phase 3 — Data Handling with NumPy and Pandas

Status: NOT STARTED

### NumPy

- NumPy arrays and array creation
- Array dimensions, shape, size and data types
- Indexing and slicing
- Reshaping and joining arrays
- Vectorized operations
- Handling missing or invalid numeric values
- Basic aggregation and statistics

### Pandas

- [CORE] Series and DataFrame
- [CORE] Creating DataFrames from lists, dictionaries and files
- [CORE] Reading and writing CSV
- [CORE] Reading and writing JSON
- Reading Excel files
- Reading Parquet files
- [CORE] Inspecting data: head, tail, info, describe, shape, columns, dtypes
- [CORE] Selecting columns and filtering rows
- [CORE] Sorting and renaming
- [CORE] Handling missing values
- [CORE] Removing duplicates
- [CORE] Changing data types
- [CORE] String operations
- [CORE] Date and time conversion
- [CORE] GroupBy and aggregations
- [CORE] Merge, join and concat
- Pivot tables and reshaping
- Applying functions: apply, map and vectorized alternatives
- [CORE] Data cleaning and standardization
- [CORE] Data validation and basic quality checks
- Processing large files in chunks
- Memory usage and efficient DataFrame operations
- Exporting transformed data

## Phase 4 — Working with APIs and Data Formats

Status: NOT STARTED

- [CORE] HTTP basics: request, response, status codes and headers
- [CORE] REST API concepts
- [CORE] Using the requests library
- GET and POST requests
- Query parameters, headers and request bodies
- [CORE] JSON responses and nested JSON
- Authentication basics: API keys, tokens and bearer tokens
- [IMPORTANT] Pagination
- [IMPORTANT] Timeouts and retry handling
- Handling rate limits
- Handling API errors and unsuccessful responses
- Parsing nested JSON into usable records
- Flattening JSON data with Pandas
- Saving API responses to files
- [IMPORTANT] API-to-CSV and API-to-JSON workflows
- Working with dates and timestamps received from APIs
- [ADDITIONAL] Introduction to asynchronous API requests

## Phase 5 — Python, SQL and Database Connectivity

Status: NOT STARTED

### Database programming concepts

- [CORE] Relational database connection concepts
- [CORE] DB-API 2.0 concepts
- Connections and cursors
- [CORE] execute() and executemany()
- [CORE] Parameterized SQL queries
- Fetching results: fetchone, fetchmany and fetchall
- Commit and rollback
- Transactions and connection handling
- [CORE] Handling database exceptions
- [IMPORTANT] Connection closing and context-manager patterns
- Batch inserts and updates
- Reading query results into Python structures and Pandas
- Writing DataFrames to databases
- Avoiding SQL injection through parameterized queries

### Snowflake with Python

- [CORE] Snowflake Connector for Python
- Creating and managing connections securely
- Executing SQL from Python
- Fetching query results
- Binding parameters safely
- Loading data using Python connector-supported methods
- Writing data from Python to Snowflake
- Error handling and connection cleanup
- [IMPORTANT] Snowpark Python basics
- Snowpark DataFrames
- Selecting, filtering and transforming with Snowpark
- Actions and lazy evaluation concepts
- Collecting results and understanding when data moves to the client

## Phase 6 — Professional and Production-Ready Python

Status: NOT STARTED

- [CORE] Classes and objects
- Constructors and instance attributes
- Instance, class and static methods
- Encapsulation and inheritance
- Composition and reusable design
- Understanding when functions are simpler than classes
- [CORE] Environment variables
- [CORE] Managing secrets and credentials safely
- Configuration files and application settings
- [CORE] Command-line arguments with argparse
- Building reusable command-line scripts
- [CORE] Logging in real projects
- Log levels, structured messages and log files
- [IMPORTANT] Python packaging basics
- Creating reusable packages
- Dependency management and version pinning
- Type hints and return types
- Docstrings and readable documentation
- Code organization and separation of responsibilities
- pathlib for cross-platform file paths
- datetime and timezone-aware timestamps
- Regular expressions for text validation and extraction
- Working with compressed files
- [IMPORTANT] Memory-efficient processing and generators
- Iterators and generators
- Decorators: basic understanding and practical use
- [ADDITIONAL] Multiprocessing and concurrent execution basics
- [ADDITIONAL] Asyncio fundamentals

## Phase 7 — Testing, Debugging and Code Quality

Status: NOT STARTED

- [CORE] Testing fundamentals
- [CORE] Assertions
- [CORE] pytest basics
- Writing and running test functions
- [CORE] Fixtures
- Test setup and teardown
- Parameterized tests
- Testing functions that transform data
- Testing file-reading and file-writing logic
- Mocking API responses
- Mocking database interactions
- Testing error conditions and edge cases
- [IMPORTANT] Debugging with breakpoints
- Reading tracebacks and diagnosing failures
- [IMPORTANT] Code formatting and linting
- Basic static checks
- Refactoring duplicated code
- Writing maintainable and testable Python

## Phase 8 — End-to-End Python Data Engineering Project

Status: NOT STARTED

Build one complete Python-based ETL project that brings together the topics above.

### Project workflow

- [CORE] Extract data from a REST API
- Handle API authentication securely
- Handle pagination, timeouts, retries and API errors
- Save raw API responses as JSON
- Read source CSV and JSON files
- Inspect and validate incoming data
- [CORE] Clean and transform data using Pandas
- Handle nulls, duplicates, incorrect data types and inconsistent values
- Convert date and timestamp columns correctly
- Apply business rules and data-quality checks
- Log each major processing step
- [CORE] Connect to Snowflake using the Python connector
- Load transformed data into Snowflake
- Use safe parameterized SQL where applicable
- Handle failed loads and database exceptions
- Keep credentials outside source code
- Use configuration and command-line arguments
- Organize the project into modules and packages
- Use a virtual environment and dependency file
- Write pytest tests for important functions
- Add clear project documentation
- Run the complete pipeline from the command line
- Verify source, transformed and loaded record counts
- Record errors and execution details in log files

### Suggested project structure

    python-data-engineering-project/
        data/
            raw/
            processed/
        logs/
        src/
            config/
            extraction/
            transformation/
            loading/
            utils/
            main.py
        tests/
        .env.example
        .gitignore
        requirements.txt
        README.md

Do not commit real credentials or secret values. Keep local secret files out of version control.

---

## Additional Python Topics Worth Knowing

Status: NOT STARTED — cover after the core phases where relevant

- [IMPORTANT] Working with dates, time zones and timestamps
- [IMPORTANT] Decimal precision for financial or exact decimal values
- [IMPORTANT] Data serialization and deserialization
- [IMPORTANT] Hashing and checksums for file validation
- [IMPORTANT] File compression: gzip and zip
- [IMPORTANT] Generators for processing data without loading everything into memory
- [IMPORTANT] Memory profiling and performance measurement basics
- [ADDITIONAL] Working with XML using Python libraries
- [ADDITIONAL] Working with Parquet and ORC through Python libraries
- [ADDITIONAL] Basic multiprocessing and concurrency
- [ADDITIONAL] Basic async programming
- [ADDITIONAL] Working with binary files and streams

---

## Recommended Priority

The most useful skills to become comfortable with first are:

1. [CORE] Python functions, collections and file handling
2. [CORE] CSV, JSON and exception handling
3. [CORE] Modules, imports and virtual environments
4. [CORE] Pandas: filtering, cleaning, merging, grouping and file I/O
5. [CORE] REST APIs, requests, JSON and pagination
6. [CORE] DB-API, parameterized SQL and database connectivity
7. [CORE] Snowflake Connector for Python
8. [CORE] Logging, configuration, environment variables and secrets
9. [CORE] pytest and testing data transformations
10. [CORE] A complete API/CSV/JSON-to-Pandas-to-Snowflake ETL project

## Completion Notes

- Phase 1 is marked COMPLETED based on the lessons already covered.
- Logging was identified as needing stronger coverage; revisit it in Phase 1 and again in Phase 6.
- The Snowflake Connector for Python has already been covered according to the learning history; revisit it during Phase 5 for revision and practical integration.
- CSV reader/DictReader practice may still need revision.
- Complete the Python roadmap before moving on to separate technologies such as ADF, CDC, incremental loading, dbt and Spark/PySpark.
