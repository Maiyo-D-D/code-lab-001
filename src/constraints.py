import os

# Get the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Input file constraints
INPUT_FILE = os.path.join(PROJECT_ROOT, 'data', 'test_files.xlsx')

# Output file constraints
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
EMAIL_OUTPUT_CSV = os.path.join(OUTPUT_DIR, 'students_with_emails.csv')
EMAIL_OUTPUT_TSV = os.path.join(OUTPUT_DIR, 'students_with_emails.tsv')
MALE_STUDENTS_CSV = os.path.join(OUTPUT_DIR, 'male_students.csv')
FEMALE_STUDENTS_CSV = os.path.join(OUTPUT_DIR, 'female_students.csv')
SPECIAL_CHAR_STUDENTS_CSV = os.path.join(OUTPUT_DIR, 'special_char_students.csv')
SHUFFLED_STUDENTS_JSON = os.path.join(OUTPUT_DIR, 'shuffled_students.json')
SHUFFLED_STUDENTS_JSONL = os.path.join(OUTPUT_DIR, 'shuffled_students.jsonl')

# Log file constraints
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
EMAIL_LOG = os.path.join(LOG_DIR, 'email_generation.log')
STUDENT_SEPARATION_LOG = os.path.join(LOG_DIR, 'student_separation.log')
NAME_SHUFFLING_LOG = os.path.join(LOG_DIR, 'name_shuffling.log')

# Email constraints
EMAIL_DOMAIN = 'gmail.com'

# Similarity threshold for name comparison (if implementing LaBSE)
SIMILARITY_THRESHOLD = 0.5