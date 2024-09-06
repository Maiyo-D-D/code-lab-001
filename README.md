Grooking Python 101
This project is part of the Grooking Python 101 assignment, focusing on data manipulation, email generation, and various data processing tasks using Python.
Project Structure
grooking-python-101/
│
├── src/
│   ├── main.py
│   ├── functions.py
│   └── constraints.py
│
├── data/
│   └── test_files.xlsx
│
├── output/
│   ├── students_with_emails.csv
│   ├── students_with_emails.tsv
│   ├── male_students.csv
│   ├── female_students.csv
│   ├── special_char_students.csv
│   ├── shuffled_students.json
│   └── shuffled_students.jsonl
│
├── logs/
│   ├── email_generation.log
│   ├── student_separation.log
│   └── name_shuffling.log
│
└── README.md


Features
Email generation for students
Separation of students by gender
Identification of students with special characters in their names
Shuffling and saving student data in JSON and JSONL formats
Comprehensive logging of operations

Requirements
Python 3.x
pandas
openpyxl (for reading Excel files)

Installation
Clone the repository:
Copygit clone https://github.com/Maiyo-D-D/code-lab-001.git
cd grooking-python-101

Create a virtual environment (optional but recommended):
Copypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
Copypip install pandas openpyxl

Usage
Place your input Excel file (test_files.xlsx) in the data/ directory.
Run the main script:
Copypython src/main.py

Check the output/ directory for the generated files and the logs/ directory for operation logs.

File Descriptions
src/main.py: The main program file that orchestrates the entire process.
src/functions.py: Contains all the utility functions used in the project.
src/constraints.py: Defines constants and file paths used throughout the project.

Output Files
students_with_emails.csv and students_with_emails.tsv: Students' information with generated email addresses.
male_students.csv and female_students.csv: Separated lists of male and female students.
special_char_students.csv: List of students with special characters in their names.
shuffled_students.json and shuffled_students.jsonl: Shuffled student data in JSON and JSONL formats.

Logs
email_generation.log: Log of email generation process.
student_separation.log: Log of student separation by gender.
name_shuffling.log: Log of name shuffling process.

Future Enhancements
Implement LaBSE for name similarity comparison (stretch goal).
Integrate with Google API for cloud storage backup.

Contributing
Please feel free to submit issues and pull requests for any improvements or bug fixes.
